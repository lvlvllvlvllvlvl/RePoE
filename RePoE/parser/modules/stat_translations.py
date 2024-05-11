from collections import defaultdict
import json
import re
from typing import Any, Dict, Iterator, List, Set, Tuple, Union

from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.translations import (
    Translation,
    TranslationString,
    TranslationFileCache,
    TranslationRange,
    TranslationQuantifier,
    TranslationQuantifierHandler,
    TQNumberFormat,
    TQRelationalData,
    get_custom_translation_file,
    install_data_dependant_quantifiers,
)
from urllib.request import urlopen, Request

from RePoE.model import stats_by_file
from RePoE.model import stat_value_handlers
from RePoE.model.stat_translations import Stat
from RePoE.parser import Parser_Module
from RePoE.parser.util import call_with_default_args, get_stat_translation_file_name, write_json, write_model


class stat_translations(Parser_Module):
    def _convert_tags(self, n_ids: int, tags: List[int], tags_types: List[str]) -> List[str]:
        f = ["ignore" for _ in range(n_ids)]
        for tag, tag_type in zip(tags, tags_types):
            if tag >= n_ids:
                continue
            if tag_type in ["+", "+d"]:
                f[tag] = "+#"
            elif tag_type == "d":
                f[tag] = "#"
            elif tag_type == "":
                f[tag] = "#"
            else:
                raise Exception("Unknown tag type:", tag_type)
        return f

    def _convert_range(self, translation_range: List[TranslationRange]) -> Union[List[Dict[str, int]], List[Dict]]:
        rs = []
        for r in translation_range:
            r_dict = {}
            if r.min is not None:
                r_dict["min"] = r.min
            if r.max is not None:
                r_dict["max"] = r.max
            if r.negated:
                r_dict["negated"] = True
            rs.append(r_dict)
        return rs

    def _convert_handlers(self, n_ids: int, index_handlers: Dict) -> Union[List[List[str]], List[List]]:
        hs: List[List[str]] = [[] for _ in range(n_ids)]
        for handler_name, ids in index_handlers.items():
            for i in ids:
                # Indices in the handler dict are 1-based
                hs[i - 1].append(handler_name)
        return hs

    def _convert(self, tr: Translation) -> Dict[str, Any]:
        ids = tr.ids
        n_ids = len(ids)
        result = []
        trade_stats = {}
        partial_trade_stats = {}
        strings = tr.get_language(self.language).strings
        result = [self._convert_translation_string(s, n_ids, trade_stats, partial_trade_stats) for s in strings]

        self._add_values_to_lookup(result, strings, ids)

        return {
            "ids": ids,
            self.language: [r for r in result if r],
            "trade_stats": (
                list(trade_stats.values())
                if trade_stats
                else list(partial_trade_stats.values())
                if partial_trade_stats
                else None
            ),
        }

    def _convert_translation_string(
        self, s: TranslationString, n_ids: int, trade_stats: dict, partial_trade_stats: dict
    ):
        try:
            tags = self._convert_tags(n_ids, s.tags, s.tags_types)
            self.tag_set.update(tags)

            def placeholder(*_):
                return "#"

            trade_format, _, _, extra_strings, _ = s.format_string(
                [1 for _ in s.translation.ids],
                [False for _ in s.translation.ids],
                use_placeholder=placeholder,
            )
            if trade_format in self.trade_stats:
                for trade_stat in self.trade_stats[trade_format]:
                    trade_stats[trade_stat["id"]] = trade_stat
            elif "\n" in trade_format:
                for line in trade_format.splitlines():
                    if line in self.trade_stats:
                        for trade_stat in self.trade_stats[line]:
                            partial_trade_stats[trade_stat["id"]] = trade_stat
            else:
                trade_format = re.sub(r"\d+", "#", trade_format)
                if trade_format in self.trade_stats:
                    for trade_stat in self.trade_stats[trade_format]:
                        trade_stats[trade_stat["id"]] = trade_stat

            value = Stat(
                condition=self._convert_range(s.range),
                string=s.as_format_string,
                format=tags,
                index_handlers=self._convert_handlers(n_ids, s.quantifier.index_handlers),
                reminder_text=next(iter(extra_strings.values())) if extra_strings else None,
            )
            if "markup" in s.quantifier.string_handlers:
                value.is_markup = True

            return value
        except Exception:
            print("Error processing", s)
            return None

    def _add_values_to_lookup(self, values: list[Stat], strings: list[TranslationString], ids: list[str]):
        for value, s in zip(values, strings):
            if not value:
                continue
            if value.string in self.lookup.root:
                self.lookup.root[value.string].files.append(self.current_file)
            else:
                try:
                    tokens = []
                    for i, tag in enumerate(s.tags):
                        if s.strings[i]:
                            tokens.append(stats_by_file.Literal(type="literal", value=s.strings[i]))
                        handler = next(
                            iter(
                                TranslationQuantifierHandler.handlers[h.root]
                                for h in value.index_handlers[tag]
                                if "canonical" not in h.root
                            ),
                            None,
                        )
                        if not handler:
                            tokens.append(stats_by_file.Number(type="number", index=tag, stat=ids[tag]))
                        elif isinstance(handler, TQNumberFormat):
                            tokens.append(
                                stats_by_file.Number(
                                    type="number",
                                    index=tag,
                                    stat=ids[tag],
                                    stat_value_handlers=[h.root for h in value.index_handlers[tag]],
                                )
                            )
                        elif isinstance(handler, TQRelationalData):
                            tokens.append(
                                stats_by_file.EnumModel(
                                    type="enum", index=tag, stat=ids[tag], stat_value_handler=handler.id
                                )
                            )
                        else:
                            tokens.append(
                                stats_by_file.Unknown(
                                    type="unknown", index=tag, stat=ids[tag], stat_value_handler=handler.id
                                )
                            )

                    if s.strings[-1]:
                        tokens.append(stats_by_file.Literal(type="literal", value=s.strings[-1]))
                    self.lookup.root[value.string] = stats_by_file.Stat(
                        files=[self.current_file], generated_name=f"Stat_{len(self.lookup.root)}", tokens=tokens
                    )
                except Exception as e:
                    print(e)

    def _get_stat_translations(
        self, translations: List[Translation], custom_translations: List[Translation]
    ) -> List[Dict[str, Any]]:
        previous = set()
        root = []
        for tr in translations:
            id_str = " ".join(tr.ids)
            if id_str in previous:
                print("Duplicate id", tr.ids)
                continue
            previous.add(id_str)
            root.append(self._convert(tr))
        for tr in custom_translations:
            id_str = " ".join(tr.ids)
            if id_str in previous:
                continue
            previous.add(id_str)
            result = self._convert(tr)
            result["hidden"] = True
            root.append(result)
        return root

    def _build_stat_translation_file_map(self, file_system: FileSystem) -> Iterator[Tuple[str, str]]:
        node = file_system.build_directory()
        for game_file in node["Metadata"]["StatDescriptions"].children.keys():
            out_file = get_stat_translation_file_name(game_file)
            if out_file:
                yield game_file, out_file

    def write(self) -> None:
        self.lookup = stats_by_file.Model({})
        install_data_dependant_quantifiers(self.relational_reader)

        quantifiers = {}
        for handler_name, handler in TranslationQuantifierHandler.handlers.items():
            if isinstance(handler, TQNumberFormat):
                quantifiers[handler_name] = stat_value_handlers.IntHandler(
                    **{
                        "type": handler.type.name.lower(),
                        "multiplier": handler.multiplier if handler.multiplier != 1 else None,
                        "divisor": handler.divisor if handler.divisor != 1 else None,
                        "addend": handler.addend if handler.addend != 0 else None,
                        "precision": handler.dp,
                        "fixed": handler.fixed if handler.fixed else None,
                    }
                )
            elif isinstance(handler, TQRelationalData):
                quantifiers[handler_name] = stat_value_handlers.RelationalData(
                    **{
                        "type": "relational",
                        "dat_file": handler.table.file_name,
                        "value_column": handler.value_column,
                        "index_column": handler.index_column,
                        "predicate": (
                            {
                                "column": handler.predicate[0],
                                "value": handler.predicate[1],
                            }
                            if handler.predicate
                            else None
                        ),
                        "values": {
                            str(r[handler.index_column] if handler.index_column else r.rowid): r[handler.value_column]
                            for r in handler.table
                            if r[handler.value_column]
                            and (not handler.predicate or r[handler.predicate[0]] == handler.predicate[1])
                        },
                    }
                )
            elif handler.type == TranslationQuantifier.QuantifierTypes.STRING:
                quantifiers[handler_name] = stat_value_handlers.CanonicalLine(type=handler.type.name.lower())
            else:
                quantifiers[handler_name] = stat_value_handlers.Noop(type="noop")
        write_json(quantifiers, self.data_path, "stat_value_handlers")

        with urlopen(
            Request(
                "https://www.pathofexile.com/api/trade/data/stats",
                headers={"User-Agent": "OAuth RePoE/1.0.0 (contact: https://github.com/lvlvllvlvllvlvl/RePoE/)"},
            )
        ) as req:
            data = json.load(req)
            if "result" not in data:
                print(data)
            self.trade_stats = defaultdict(list)
            for trade_stat in [entry for v in data["result"] for entry in v["entries"]]:
                if "option" in trade_stat:
                    for option in trade_stat["option"]["options"]:
                        self.trade_stats[trade_stat["text"].replace("#", option["text"])].append(trade_stat)
                else:
                    self.trade_stats[trade_stat["text"]].append(trade_stat)
            for k, v in self.trade_stats.items():
                self.trade_stats[k] = sorted(v, key=lambda v: v.get("id", ""))

        self.tag_set: Set[str] = set()

        for in_file, out_file in self._build_stat_translation_file_map(self.file_system):
            try:
                self.current_file = out_file
                tf = self.get_cache(TranslationFileCache)[in_file]
                translations = tf.translations
                result = self._get_stat_translations(translations, get_custom_translation_file().translations)
                write_json(result, self.data_path, out_file)
            except Exception:
                print("Error processing", in_file)
                raise
        clientstrings = self.relational_reader["ClientStrings.dat64"]
        for stat, stringid in list(tf._CLIENT_STRINGS_LOOKUP.items()) + [
            ("", "StatDescripotionTreeExpansionJewelGrantedSmallStat")
        ]:
            clientstring: str = clientstrings.index["Id"][stringid]["Text"]
            tokens = intersperse(clientstring.split("{0}"), stat)
            self.lookup.root[clientstring] = stats_by_file.Stat(
                files=[], generated_name=f"ClientStrings_{stringid}", tokens=tokens
            )
        write_model(self.lookup, self.data_path, "stats_by_file")
        print("Possible format tags: {}".format(self.tag_set))


# https://stackoverflow.com/a/5921708/2063518
def intersperse(tokens, stat):
    result = [None] * (len(tokens) * 2 - 1)
    result[0::2] = tokens
    return [
        (
            stats_by_file.Literal(type="literal", value=r)
            if r
            else stats_by_file.NestedStat(type="nested", added_stat=stat)
        )
        for r in result
        if r != ""
    ]


if __name__ == "__main__":
    call_with_default_args(stat_translations)
