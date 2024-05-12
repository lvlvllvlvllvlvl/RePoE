# generated by datamodel-codegen:
#   filename:  stats_by_file.schema.json

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel


class Type(Enum):
    literal = "literal"


class Literal(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Type
    value: str


class Type1(Enum):
    number = "number"


class Number(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Type1
    index: int
    stat: str
    stat_value_handlers: Optional[List[str]] = None


class Type2(Enum):
    enum = "enum"


class EnumModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Type2
    index: int
    stat: str
    stat_value_handler: str = Field(
        ..., description="Reference to the entry in stat_value_handlers.json where the enum values can be found."
    )


class Type3(Enum):
    unknown = "unknown"


class Unknown(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Type3
    index: int
    stat: str
    stat_value_handler: Optional[str] = None


class Type4(Enum):
    nested = "nested"


class NestedStat(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    type: Type4
    added_stat: str


class Token(RootModel[Union[Literal, Number, EnumModel, Unknown, NestedStat]]):
    root: Union[Literal, Number, EnumModel, Unknown, NestedStat]


class Stat(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    files: List[str]
    generated_name: str
    tokens: List[Token]
    implied_stats: Optional[Dict[str, int]] = None


class Model(RootModel[Optional[Dict[str, Stat]]]):
    root: Optional[Dict[str, Stat]] = None
