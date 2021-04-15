# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..uac import FeatureFlags_pb2 as uac_dot_FeatureFlags__pb2


class FeatureFlagsServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getFeatureFlags = channel.unary_unary(
        '/ai.verta.uac.FeatureFlagsService/getFeatureFlags',
        request_serializer=uac_dot_FeatureFlags__pb2.FeatureFlagsRequest.SerializeToString,
        response_deserializer=uac_dot_FeatureFlags__pb2.FeatureFlagsRequest.Response.FromString,
        )


class FeatureFlagsServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getFeatureFlags(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FeatureFlagsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getFeatureFlags': grpc.unary_unary_rpc_method_handler(
          servicer.getFeatureFlags,
          request_deserializer=uac_dot_FeatureFlags__pb2.FeatureFlagsRequest.FromString,
          response_serializer=uac_dot_FeatureFlags__pb2.FeatureFlagsRequest.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.FeatureFlagsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))