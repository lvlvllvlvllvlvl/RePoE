from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class cost_types(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        root = {}
        for row in relational_reader["CostTypes.dat64"]:
            root[row["Id"]] = {
                "stat": row["StatsKey"]["Id"] if row["StatsKey"] else None,
                "format_text": row["FormatText"],
            }
        write_json(root, data_path, "cost_types")


if __name__ == "__main__":
    call_with_default_args(cost_types.write)
