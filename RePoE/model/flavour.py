# generated by datamodel-codegen:
#   filename:  flavour.schema.json
#   timestamp: 2024-05-08T08:33:06+00:00

from __future__ import annotations

from typing import Dict, Optional

from pydantic import RootModel


class Model(RootModel[Optional[Dict[str, str]]]):
    root: Optional[Dict[str, str]] = None
