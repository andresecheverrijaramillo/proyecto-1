from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["id_product"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    id_product: int
    def __init__(self, id_product: _Optional[int] = ...) -> None: ...

class ProductList(_message.Message):
    __slots__ = ["product_ids"]
    PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
    product_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, product_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...
