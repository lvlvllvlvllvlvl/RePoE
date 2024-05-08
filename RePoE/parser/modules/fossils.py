from RePoE.parser import Parser_Module
from RePoE.parser.util import write_json, call_with_default_args


class fossils(Parser_Module):
    def write(self) -> None:
        root = {}
        for row in self.relational_reader["DelveCraftingModifiers.dat64"]:

            base_item_key = row["BaseItemTypesKey"]["Id"]
            name_from_base_item = row["BaseItemTypesKey"]["Name"]

            root[base_item_key] = {
                "name": name_from_base_item,
                "added_mods": [mod["Id"] for mod in row["AddedModsKeys"]],
                "forced_mods": [mod["Id"] for mod in row["ForcedAddModsKeys"]],
                "negative_mod_weights": [
                    {"tag": tag["Id"], "weight": value}
                    for tag, value in zip(row["NegativeWeight_TagsKeys"], row["NegativeWeight_Values"])
                ],
                "positive_mod_weights": [
                    {"tag": tag["Id"], "weight": value}
                    for tag, value in zip(row["Weight_TagsKeys"], row["Weight_Values"])
                ],
                "forbidden_tags": [tag["TagsKey"]["Id"] for tag in row["ForbiddenDelveCraftingTagsKeys"]],
                "allowed_tags": [tag["TagsKey"]["Id"] for tag in row["AllowedDelveCraftingTagsKeys"]],
                "corrupted_essence_chance": row["CorruptedEssenceChance"],
                "mirrors": row["CanMirrorItem"],
                "changes_quality": row["CanImproveQuality"],
                "rolls_lucky": row["HasLuckyRolls"],
                "rolls_white_sockets": row["CanRollWhiteSockets"],
                "sell_price_mods": [mod["Id"] for mod in row["SellPrice_ModsKeys"]],
                "descriptions": {
                    description["Id"]: description["Description"]
                    for description in row["DelveCraftingModifierDescriptionsKeys"]
                },
                "blocked_descriptions": {
                    description["Id"]: description["Description"]
                    for description in row["BlockedDelveCraftingModifierDescriptionsKeys"]
                },
            }

        write_json(root, self.data_path, "fossils")


if __name__ == "__main__":
    call_with_default_args(fossils)
