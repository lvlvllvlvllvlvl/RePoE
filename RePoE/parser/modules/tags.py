from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class tags(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        tags = [row["Id"] for row in relational_reader["Tags.dat64"]]
        write_json(tags, data_path, "tags")


if __name__ == "__main__":
    call_with_default_args(tags.write)
