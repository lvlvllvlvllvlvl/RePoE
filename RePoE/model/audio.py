# generated by datamodel-codegen:
#   filename:  audio.schema.json
#   timestamp: 2024-05-08T03:19:21+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class Npc(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    id: str
    name: str
    short_name: str


class Stereo(RootModel[str]):
    root: str


class Video(RootModel[str]):
    root: str


class AudioSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    mono: str
    npcs: List[Npc]
    stereo: Stereo
    text: str
    video: Video


class Model(RootModel[Optional[Dict[str, AudioSchemaValue]]]):
    root: Optional[Dict[str, AudioSchemaValue]] = None
