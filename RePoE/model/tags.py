# generated by datamodel-codegen:
#   filename:  tags.schema.json

from __future__ import annotations

from typing import List

from pydantic import RootModel


class Model(RootModel[List[str]]):
    root: List[str]
