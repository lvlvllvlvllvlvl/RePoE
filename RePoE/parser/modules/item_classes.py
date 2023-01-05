from RePoE.parser.util import call_with_default_args, write_json, get_id_or_none
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class item_classes(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        item_classes = {
            row["Id"]: {
                "name": row["Name"],
            }
            for row in relational_reader["ItemClasses.dat64"]
        }
        write_json(item_classes, data_path, "item_classes")


if __name__ == "__main__":
    call_with_default_args(item_classes.write)
