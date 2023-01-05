from RePoE.parser import Parser_Module
from RePoE.parser.util import write_json, call_with_default_args
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class gem_tags(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        root = {}
        for tag in relational_reader["GemTags.dat64"]:
            name = tag["Tag"]
            root[tag["Id"]] = name if name != "" else None
        write_json(root, data_path, "gem_tags")


if __name__ == "__main__":
    call_with_default_args(gem_tags.write)
