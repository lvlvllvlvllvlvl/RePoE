from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class active_skill_types(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        types = [row["Id"] for row in relational_reader["ActiveSkillType.dat64"]]
        write_json(types, data_path, "active_skill_types")


if __name__ == "__main__":
    call_with_default_args(active_skill_types.write)
