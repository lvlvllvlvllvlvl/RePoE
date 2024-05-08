# generated by datamodel-codegen:
#   filename:  base_items.schema.json
#   timestamp: 2024-05-08T08:33:00+00:00

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class GrantsBuff(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: str
    stats: Dict[str, int]


class Armour(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    max: int
    min: int


class Requirements(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dexterity: int
    intelligence: int
    level: int
    strength: int


class VisualIdentity(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dds_file: str
    id: str


class Domain(RootModel[str]):
    root: str


class ItemClass(RootModel[str]):
    root: str


class ReleaseState(Enum):
    released = 'released'
    unique_only = 'unique_only'
    unreleased = 'unreleased'
    legacy = 'legacy'


class Tag(RootModel[str]):
    root: str


class Properties(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    armour: Optional[Armour] = None
    energy_shield: Optional[Armour] = None
    evasion: Optional[Armour] = None
    movement_speed: Optional[int] = None
    block: Optional[int] = None
    description: Optional[str] = None
    directions: Optional[str] = None
    stack_size: Optional[int] = None
    stack_size_currency_tab: Optional[int] = None
    full_stack_turns_into: Optional[str] = None
    charges_max: Optional[int] = None
    charges_per_use: Optional[int] = None
    duration: Optional[int] = None
    life_per_use: Optional[int] = None
    mana_per_use: Optional[int] = None
    attack_time: Optional[int] = None
    critical_strike_chance: Optional[int] = None
    physical_damage_max: Optional[int] = None
    physical_damage_min: Optional[int] = None
    range: Optional[int] = None


class BaseItemsSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    domain: Domain
    drop_level: int
    implicits: List[str]
    inventory_height: int
    inventory_width: int
    item_class: ItemClass
    name: str
    properties: Properties
    release_state: ReleaseState
    tags: List[Tag]
    visual_identity: VisualIdentity
    requirements: Optional[Requirements] = None
    grants_buff: Optional[GrantsBuff] = None


class Model(RootModel[Optional[Dict[str, BaseItemsSchemaValue]]]):
    root: Optional[Dict[str, BaseItemsSchemaValue]] = None
