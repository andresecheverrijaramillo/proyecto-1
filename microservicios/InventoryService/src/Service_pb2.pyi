from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Inventory(_message.Message):
    __slots__ = ["Inv"]
    INV_FIELD_NUMBER: _ClassVar[int]
    Inv: str
    def __init__(self, Inv: _Optional[str] = ...) -> None: ...

class LastIdd(_message.Message):
    __slots__ = ["LIdd"]
    LIDD_FIELD_NUMBER: _ClassVar[int]
    LIdd: str
    def __init__(self, LIdd: _Optional[str] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...

class product(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
