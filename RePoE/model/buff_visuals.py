# generated by datamodel-codegen:
#   filename:  buff_visuals.schema.json

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class Category(Enum):
    Debuff = "Debuff"
    Charge = "Charge"
    Buff = "Buff"
    Active_skill = "Active skill"
    Aspect = "Aspect"
    PVP_team = "PVP team"
    Link = "Link"
    PVP_flag = "PVP flag"
    Mark = "Mark"
    Hex = "Hex"
    Stolen = "Stolen"
    Flask = "Flask"
    Labyrinth_trap = "Labyrinth trap"
    Herald = "Herald"
    Buff_shrine = "Buff shrine"
    Spell_shrine = "Spell shrine"
    Tincture = "Tincture"


class Source(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: Optional[str] = None
    buff_id: Optional[str] = None
    buff_category: Optional[Category] = None
    item: Optional[str] = None
    description: Optional[str] = None
    name: Optional[str] = None


class Sources(RootModel[Optional[Dict[str, List[Source]]]]):
    root: Optional[Dict[str, List[Source]]] = None


class BuffVisualsSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    description: Optional[str] = None
    icon: Optional[str] = None
    name: Optional[str] = None
    sources: Optional[Sources] = None
    sounds: Optional[List[str]] = None
    custom_frame: Optional[str] = None


class Model(RootModel[Optional[Dict[str, BuffVisualsSchemaValue]]]):
    root: Optional[Dict[str, BuffVisualsSchemaValue]] = None
