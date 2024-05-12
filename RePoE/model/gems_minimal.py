# generated by datamodel-codegen:
#   filename:  gems_minimal.schema.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class Costs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    Mana: Optional[int] = None
    ManaPercent: Optional[int] = None


class QualityStat(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    stat: str
    stats: Dict[str, int]


class Reservations(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    mana_percent: Optional[float] = None
    mana_flat: Optional[int] = None


class StatRequirements(BaseModel):
    int: Optional[Any] = None
    str: Optional[Any] = None
    dex: Optional[Any] = None


class Vaal(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    souls: int
    stored_uses: int


class MinionTypeElement(RootModel[str]):
    root: str


class WeaponRestriction(RootModel[str]):
    root: str


class ExperienceType(RootModel[str]):
    root: str


class ReleaseState(Enum):
    released = "released"
    unreleased = "unreleased"
    legacy = "legacy"


class Color(Enum):
    b = "b"
    r = "r"
    g = "g"
    w = "w"


class Discriminator(Enum):
    alt_x = "alt_x"
    alt_y = "alt_y"


class Class(RootModel[str]):
    root: str


class StatTranslationFile(RootModel[str]):
    root: str


class CooldownBypassType(Enum):
    expend_frenzy_charge = "expend_frenzy_charge"
    expend_power_charge = "expend_power_charge"
    expend_endurance_charge = "expend_endurance_charge"


class StatType(Enum):
    float = "float"
    constant = "constant"
    additional = "additional"
    implicit = "implicit"
    flag = "flag"


class Tag(RootModel[str]):
    root: str


class ActiveSkill(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: str
    display_name: str
    id: str
    is_manually_casted: bool
    is_skill_totem: bool
    stat_conversions: Dict[str, str]
    types: List[MinionTypeElement]
    weapon_restrictions: List[WeaponRestriction]
    minion_types: Optional[List[MinionTypeElement]] = None
    skill_totem_life_multiplier: Optional[float] = None


class BaseItem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    display_name: str
    experience_type: ExperienceType
    id: str
    max_level: int
    release_state: ReleaseState


class QuestReward(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    act: int
    classes: List[Class]
    quest: str


class Stat(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Optional[str] = None
    type: StatType
    value: Optional[int] = None


class SupportGem(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    allowed_types: Optional[List[MinionTypeElement]] = None
    letter: str
    supports_gems_only: bool
    excluded_types: Optional[List[MinionTypeElement]] = None
    added_types: Optional[List[MinionTypeElement]] = None
    added_minion_types: Optional[List[MinionTypeElement]] = None


class Static(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    crit_chance: Optional[int] = None
    damage_effectiveness: Optional[int] = None
    quality_stats: List[QualityStat]
    stat_requirements: StatRequirements
    stat_text: Optional[Dict[str, str]] = None
    stats: Optional[List[Optional[Stat]]] = None
    vaal: Optional[Vaal] = None
    costs: Optional[Costs] = None
    attack_speed_multiplier: Optional[int] = None
    cooldown: Optional[int] = None
    stored_uses: Optional[int] = None
    cost_multiplier: Optional[int] = None
    cooldown_bypass_type: Optional[CooldownBypassType] = None
    required_level: Optional[int] = None
    experience: Optional[int] = None
    reservations: Optional[Reservations] = None
    damage_multiplier: Optional[int] = None


class GemsMinimalSchemaElement(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    active_skill: Optional[ActiveSkill] = None
    base_item: BaseItem
    cast_time: Optional[int] = None
    color: Color
    display_name: str
    is_support: bool
    stat_translation_file: StatTranslationFile
    static: Static
    tags: List[Tag]
    secondary_granted_effect: Optional[str] = None
    quest_reward: Optional[QuestReward] = None
    discriminator: Optional[Discriminator] = None
    support_gem: Optional[SupportGem] = None


class Model(RootModel[List[GemsMinimalSchemaElement]]):
    root: List[GemsMinimalSchemaElement]
