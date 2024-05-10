# generated by datamodel-codegen:
#   filename:  gem_tags.schema.json

from __future__ import annotations

from typing import Dict, Optional

from pydantic import RootModel


class GemTagsSchema(RootModel[Optional[Dict[str, Optional[str]]]]):
    root: Optional[Dict[str, Optional[str]]] = None


class Model(RootModel[GemTagsSchema]):
    root: GemTagsSchema
