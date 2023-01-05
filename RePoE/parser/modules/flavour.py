from RePoE.parser.util import write_json, call_with_default_args
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class flavour(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        root = {}
        for flavour in relational_reader["FlavourText.dat64"]:
            if flavour["Id"] in root:
                print("Duplicate flavour id:", flavour["Id"])
            else:
                root[flavour["Id"]] = flavour["Text"]

        write_json(root, data_path, "flavour")


if __name__ == "__main__":
    call_with_default_args(flavour.write)
