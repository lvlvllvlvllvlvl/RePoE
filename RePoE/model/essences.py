# generated by datamodel-codegen:
#   filename:  essences.schema.json
#   timestamp: 2024-05-08T08:33:05+00:00

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, Field, RootModel


class Type(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    is_corruption_only: bool
    tier: int


class EssenceMods(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    Amulet: Optional[str] = None
    Belt: Optional[str] = None
    Body_Armour: Optional[str] = Field(None, alias='Body Armour')
    Boots: Optional[str] = None
    Bow: Optional[str] = None
    Claw: Optional[str] = None
    Dagger: Optional[str] = None
    Gloves: Optional[str] = None
    Helmet: Optional[str] = None
    One_Hand_Axe: Optional[str] = Field(None, alias='One Hand Axe')
    One_Hand_Mace: Optional[str] = Field(None, alias='One Hand Mace')
    One_Hand_Sword: Optional[str] = Field(None, alias='One Hand Sword')
    Quiver: Optional[str] = None
    Ring: Optional[str] = None
    Sceptre: Optional[str] = None
    Shield: Optional[str] = None
    Staff: Optional[str] = None
    Thrusting_One_Hand_Sword: Optional[str] = Field(None, alias='Thrusting One Hand Sword')
    Two_Hand_Axe: Optional[str] = Field(None, alias='Two Hand Axe')
    Two_Hand_Mace: Optional[str] = Field(None, alias='Two Hand Mace')
    Two_Hand_Sword: Optional[str] = Field(None, alias='Two Hand Sword')
    Wand: Optional[str] = None


class Essence(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    item_level_restriction: Optional[int] = None
    level: int
    mods: Optional[EssenceMods] = None
    name: str
    spawn_level_min: int
    type: Type


class EssencesSchema(RootModel[Optional[Dict[str, Essence]]]):
    root: Optional[Dict[str, Essence]] = None


class Model(RootModel[EssencesSchema]):
    root: EssencesSchema
