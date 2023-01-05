from RePoE.parser.util import call_with_default_args, write_json
from RePoE.parser import Parser_Module
from PyPoE.poe.file.dat import RelationalReader
from PyPoE.poe.file.file_system import FileSystem
from PyPoE.poe.file.ot import OTFileCache
from PyPoE.poe.file.translations import TranslationFileCache


class cluster_jewel_notables(Parser_Module):
    @staticmethod
    def write(
        file_system: FileSystem,
        data_path: str,
        relational_reader: RelationalReader,
        translation_file_cache: TranslationFileCache,
        ot_file_cache: OTFileCache,
    ) -> None:
        data = []
        for row in relational_reader["PassiveTreeExpansionSpecialSkills.dat64"]:
            data.append(
                {
                    "id": row["PassiveSkillsKey"]["Id"],
                    "name": row["PassiveSkillsKey"]["Name"],
                    "jewel_stat": row["StatsKey"]["Id"],
                }
            )
        write_json(data, data_path, "cluster_jewel_notables")


if __name__ == "__main__":
    call_with_default_args(cluster_jewel_notables.write)
