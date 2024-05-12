# generated by datamodel-codegen:
#   filename:  fossils.schema.json

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel


class TiveModWeight(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tag: str
    weight: int


class FossilsSchema1(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    added_mods: List[str]
    allowed_tags: List[str]
    blocked_descriptions: Dict[str, str]
    changes_quality: bool
    corrupted_essence_chance: int
    descriptions: Dict[str, str]
    forbidden_tags: List[str]
    forced_mods: List[str]
    mirrors: bool
    name: str
    negative_mod_weights: List[TiveModWeight]
    positive_mod_weights: List[TiveModWeight]
    rolls_lucky: bool
    rolls_white_sockets: bool
    sell_price_mods: List[str]


class FossilsSchema(RootModel[Optional[Dict[str, FossilsSchema1]]]):
    root: Optional[Dict[str, FossilsSchema1]] = Field(None, title="MetadataItemsCurrencyCurrencyDelveCraftingAbyss")


class Model(RootModel[FossilsSchema]):
    root: FossilsSchema
