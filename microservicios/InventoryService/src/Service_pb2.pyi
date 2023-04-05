from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Inventory(_message.Message):
    __slots__ = ["Inventory"]
    INVENTORY_FIELD_NUMBER: _ClassVar[int]
    Inventory: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, Inventory: _Optional[_Iterable[int]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
