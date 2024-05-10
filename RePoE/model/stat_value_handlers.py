# generated by datamodel-codegen:
#   filename:  stat_value_handlers.schema.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional, Union

from pydantic import BaseModel, ConfigDict, RootModel, constr


class Type(Enum):
    int = 'int'


class IntHandler(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    addend: Optional[float] = None
    divisor: Optional[float] = None
    multiplier: Optional[float] = None
    precision: Optional[int] = None
    fixed: Optional[bool] = None
    type: Type


class Type1(Enum):
    relational = 'relational'


class Predicate(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    column: Optional[str] = None
    value: Optional[Any] = None


class Type2(Enum):
    string = 'string'


class CanonicalLine(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Type2


class Type3(Enum):
    noop = 'noop'


class Noop(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    type: Type3


class RelationalData(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
    )
    dat_file: str
    index_column: Optional[str] = None
    type: Type1
    value_column: str
    values: Dict[constr(pattern=r'^\d+$'), str]
    predicate: Optional[Predicate] = None


class StatValueHandlersSchema(RootModel[Optional[Dict[str, Union[IntHandler, RelationalData, CanonicalLine, Noop]]]]):
    root: Optional[Dict[str, Union[IntHandler, RelationalData, CanonicalLine, Noop]]] = None


class Model(RootModel[StatValueHandlersSchema]):
    root: StatValueHandlersSchema
