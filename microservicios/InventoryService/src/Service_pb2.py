# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rService.proto\"\x18\n\tInventory\x12\x0b\n\x03Inv\x18\x01 \x01(\t\"\t\n\x07Request\"\x17\n\x07LastIdd\x12\x0c\n\x04LIdd\x18\x01 \x01(\t\"#\n\x07product\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"*\n\x13TransactionResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x32\x8f\x01\n\x10InventoryService\x12&\n\x0cGetInventory\x12\x08.Request\x1a\n.Inventory\"\x00\x12\"\n\nGetLastIdd\x12\x08.Request\x1a\x08.LastIdd\"\x00\x12/\n\x0b\x61\x64\x64Products\x12\x08.product\x1a\x14.TransactionResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVENTORY._serialized_start=17
  _INVENTORY._serialized_end=41
  _REQUEST._serialized_start=43
  _REQUEST._serialized_end=52
  _LASTIDD._serialized_start=54
  _LASTIDD._serialized_end=77
  _PRODUCT._serialized_start=79
  _PRODUCT._serialized_end=114
  _TRANSACTIONRESPONSE._serialized_start=116
  _TRANSACTIONRESPONSE._serialized_end=158
  _INVENTORYSERVICE._serialized_start=161
  _INVENTORYSERVICE._serialized_end=304
# @@protoc_insertion_point(module_scope)
