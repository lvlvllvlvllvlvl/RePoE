# generated by datamodel-codegen:
#   filename:  tags.schema.json
#   timestamp: 2024-05-08T10:03:28+00:00

from __future__ import annotations

from typing import List

from pydantic import RootModel


class Model(RootModel[List[str]]):
    root: List[str]
