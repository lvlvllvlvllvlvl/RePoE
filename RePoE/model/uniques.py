# generated by datamodel-codegen:
#   filename:  uniques.schema.json
#   timestamp: 2024-05-08T08:05:19+00:00

from __future__ import annotations

from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class Version(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    name: str
    rowid: int


class VisualIdentity(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dds_file: str
    id: str


class ItemClass(RootModel[str]):
    root: str


class UniquesSchemaValue(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    id: str
    inventory_height: int
    inventory_width: int
    is_alternate_art: bool
    item_class: ItemClass
    name: str
    visual_identity: VisualIdentity
    renamed_version: Optional[Version] = None
    base_version: Optional[Version] = None


class Model(RootModel[Optional[Dict[str, UniquesSchemaValue]]]):
    root: Optional[Dict[str, UniquesSchemaValue]] = None
