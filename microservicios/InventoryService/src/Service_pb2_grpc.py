# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Service_pb2 as Service__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInventory = channel.unary_unary(
                '/InventoryService/GetInventory',
                request_serializer=Service__pb2.Request.SerializeToString,
                response_deserializer=Service__pb2.Inventory.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetInventory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInventory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInventory,
                    request_deserializer=Service__pb2.Request.FromString,
                    response_serializer=Service__pb2.Inventory.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetInventory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/GetInventory',
            Service__pb2.Request.SerializeToString,
            Service__pb2.Inventory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)