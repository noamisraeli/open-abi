import typing

import pydantic


SolidityType = typing.Literal[
    'uint256',
    'uint8',
    'bytes32', 
    'address',
    'string',
    'bool'
]

StateMutabilityType = typing.Literal[
    'nonpayable',
    'pure',
    'view',
    'payable'
]

class Attribute(pydantic.BaseModel):
    name: str

class Argument(pydantic.BaseModel):
    name: str
    type: SolidityType


class ConstructorAttribute(pydantic.BaseModel):
    type: typing.Literal['constructor']
    stateMutability: StateMutabilityType
    payable: bool
    inputs: typing.List[Argument]


class FunctionAttribute(pydantic.BaseModel):
    type: typing.Literal['function']
    name: str
    constant = False
    stateMutability: StateMutabilityType
    payable: bool
    inputs: typing.List[Argument]
    outputs: typing.List[Argument]


class EventParam(pydantic.BaseModel):
    indexed: bool
    name: str
    type: SolidityType


class EventAttribute(pydantic.BaseModel):
    type: typing.Literal['event']
    inputs: typing.List[EventParam]
    name: str
    anonymous: bool


class FallbackFunctionAttribute(pydantic.BaseModel):
    type: typing.Literal['fallback']
    stateMutability: StateMutabilityType
    payable: bool
