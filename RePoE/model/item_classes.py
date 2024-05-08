# generated by datamodel-codegen:
#   filename:  item_classes.schema.json
#   timestamp: 2024-05-08T08:33:10+00:00

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class ItemClassesSchema1(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    category: Optional[str] = None
    category_id: Optional[str] = None
    name: str
    influence_tags: Optional[List[str]] = None


class ItemClassesSchema(RootModel[Optional[Dict[str, ItemClassesSchema1]]]):
    root: Optional[Dict[str, ItemClassesSchema1]] = None


class Model(RootModel[ItemClassesSchema]):
    root: ItemClassesSchema
