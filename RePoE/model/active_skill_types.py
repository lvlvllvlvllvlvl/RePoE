# generated by datamodel-codegen:
#   filename:  active_skill_types.schema.json
#   timestamp: 2024-05-08T08:32:58+00:00

from __future__ import annotations

from typing import List

from pydantic import RootModel


class Model(RootModel[List[str]]):
    root: List[str]
