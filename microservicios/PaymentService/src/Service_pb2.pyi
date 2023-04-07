from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Productps(_message.Message):
    __slots__ = ["id_product", "name", "userName"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    id_product: str
    name: str
    userName: str
    def __init__(self, id_product: _Optional[str] = ..., name: _Optional[str] = ..., userName: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...
