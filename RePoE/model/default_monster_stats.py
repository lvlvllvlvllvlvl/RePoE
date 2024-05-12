# generated by datamodel-codegen:
#   filename:  default_monster_stats.schema.json

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class DefaultMonsterStatsSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    accuracy: int
    ally_life: int
    armour: int
    evasion: int
    life: int
    physical_damage: float


class Model(RootModel[Optional[Dict[str, DefaultMonsterStatsSchemaValue]]]):
    root: Optional[Dict[str, DefaultMonsterStatsSchemaValue]] = None
