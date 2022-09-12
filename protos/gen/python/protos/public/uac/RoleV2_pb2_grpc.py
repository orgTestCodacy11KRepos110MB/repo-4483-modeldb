# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..uac import RoleV2_pb2 as uac_dot_RoleV2__pb2


class RoleServiceV2Stub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.setRole = channel.unary_unary(
        '/ai.verta.uac.RoleServiceV2/setRole',
        request_serializer=uac_dot_RoleV2__pb2.SetRoleV2.SerializeToString,
        response_deserializer=uac_dot_RoleV2__pb2.SetRoleV2.Response.FromString,
        )
    self.deleteRole = channel.unary_unary(
        '/ai.verta.uac.RoleServiceV2/deleteRole',
        request_serializer=uac_dot_RoleV2__pb2.DeleteRoleV2.SerializeToString,
        response_deserializer=uac_dot_RoleV2__pb2.DeleteRoleV2.Response.FromString,
        )
    self.searchRoles = channel.unary_unary(
        '/ai.verta.uac.RoleServiceV2/searchRoles',
        request_serializer=uac_dot_RoleV2__pb2.SearchRolesV2.SerializeToString,
        response_deserializer=uac_dot_RoleV2__pb2.SearchRolesV2.Response.FromString,
        )


class RoleServiceV2Servicer(object):
  # missing associated documentation comment in .proto file
  pass

  def setRole(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteRole(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def searchRoles(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RoleServiceV2Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'setRole': grpc.unary_unary_rpc_method_handler(
          servicer.setRole,
          request_deserializer=uac_dot_RoleV2__pb2.SetRoleV2.FromString,
          response_serializer=uac_dot_RoleV2__pb2.SetRoleV2.Response.SerializeToString,
      ),
      'deleteRole': grpc.unary_unary_rpc_method_handler(
          servicer.deleteRole,
          request_deserializer=uac_dot_RoleV2__pb2.DeleteRoleV2.FromString,
          response_serializer=uac_dot_RoleV2__pb2.DeleteRoleV2.Response.SerializeToString,
      ),
      'searchRoles': grpc.unary_unary_rpc_method_handler(
          servicer.searchRoles,
          request_deserializer=uac_dot_RoleV2__pb2.SearchRolesV2.FromString,
          response_serializer=uac_dot_RoleV2__pb2.SearchRolesV2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.RoleServiceV2', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))