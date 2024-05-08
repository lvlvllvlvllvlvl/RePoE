# generated by datamodel-codegen:
#   filename:  mods.schema.json
#   timestamp: 2024-05-08T08:33:12+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class GrantsEffect(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    granted_effect_id: str
    level: int


class Stat(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: str
    max: int
    min: int


class AddsTag(RootModel[str]):
    root: str


class Domain(RootModel[str]):
    root: str


class GenerationType(RootModel[str]):
    root: str


class Tag(RootModel[str]):
    root: str


class ImplicitTag(RootModel[str]):
    root: str


class NWeight(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    tag: Tag
    weight: int


class ModsSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    adds_tags: List[AddsTag]
    domain: Domain
    generation_type: GenerationType
    generation_weights: List[NWeight]
    grants_effects: List[GrantsEffect]
    groups: List[str]
    implicit_tags: List[ImplicitTag]
    is_essence_only: bool
    name: str
    required_level: int
    spawn_weights: List[NWeight]
    stats: List[Stat]
    text: Optional[str] = None
    type: str


class Model(RootModel[Optional[Dict[str, ModsSchemaValue]]]):
    root: Optional[Dict[str, ModsSchemaValue]] = None
