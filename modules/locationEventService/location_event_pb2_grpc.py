# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import location_event_pb2 as location__event__pb2


class EventLocationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServerResponse = channel.unary_unary(
                '/EventLocationService/GetServerResponse',
                request_serializer=location__event__pb2.EventLocationMessage.SerializeToString,
                response_deserializer=location__event__pb2.EventLocationMessage.FromString,
                )


class EventLocationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServerResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventLocationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServerResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerResponse,
                    request_deserializer=location__event__pb2.EventLocationMessage.FromString,
                    response_serializer=location__event__pb2.EventLocationMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EventLocationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventLocationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EventLocationService/GetServerResponse',
            location__event__pb2.EventLocationMessage.SerializeToString,
            location__event__pb2.EventLocationMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
