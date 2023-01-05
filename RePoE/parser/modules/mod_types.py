from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class mod_types(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        mod_types = {
            row["Name"]: {
                "sell_price_types": [key["Id"] for key in row["ModSellPriceTypesKeys"]],
            }
            for row in relational_reader["ModType.dat64"]
        }

        write_json(mod_types, data_path, "mod_types")


if __name__ == "__main__":
    call_with_default_args(mod_types.write)
