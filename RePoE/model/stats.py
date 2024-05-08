# generated by datamodel-codegen:
#   filename:  stats.schema.json
#   timestamp: 2024-05-08T08:05:17+00:00

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class Alias(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    when_in_off_hand: Optional[str] = None
    when_in_main_hand: Optional[str] = None


class StatsSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    alias: Alias
    is_aliased: bool
    is_local: bool


class Model(RootModel[Optional[Dict[str, StatsSchemaValue]]]):
    root: Optional[Dict[str, StatsSchemaValue]] = None
