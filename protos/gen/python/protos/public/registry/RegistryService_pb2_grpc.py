# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..registry import RegistryService_pb2 as registry_dot_RegistryService__pb2


class RegistryServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FindRegisteredModel = channel.unary_unary(
        '/ai.verta.registry.RegistryService/FindRegisteredModel',
        request_serializer=registry_dot_RegistryService__pb2.FindRegisteredModelRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.FindRegisteredModelRequest.Response.FromString,
        )
    self.GetRegisteredModel = channel.unary_unary(
        '/ai.verta.registry.RegistryService/GetRegisteredModel',
        request_serializer=registry_dot_RegistryService__pb2.GetRegisteredModelRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.GetRegisteredModelRequest.Response.FromString,
        )
    self.GetRegisteredModelCount = channel.unary_unary(
        '/ai.verta.registry.RegistryService/GetRegisteredModelCount',
        request_serializer=registry_dot_RegistryService__pb2.GetRegisteredModelCountRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.GetRegisteredModelCountRequest.Response.FromString,
        )
    self.CreateRegisteredModel = channel.unary_unary(
        '/ai.verta.registry.RegistryService/CreateRegisteredModel',
        request_serializer=registry_dot_RegistryService__pb2.SetRegisteredModel.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetRegisteredModel.Response.FromString,
        )
    self.UpdateRegisteredModel = channel.unary_unary(
        '/ai.verta.registry.RegistryService/UpdateRegisteredModel',
        request_serializer=registry_dot_RegistryService__pb2.SetRegisteredModel.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetRegisteredModel.Response.FromString,
        )
    self.DeleteRegisteredModel = channel.unary_unary(
        '/ai.verta.registry.RegistryService/DeleteRegisteredModel',
        request_serializer=registry_dot_RegistryService__pb2.DeleteRegisteredModelRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.DeleteRegisteredModelRequest.Response.FromString,
        )
    self.FindModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/FindModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.FindModelVersionRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.FindModelVersionRequest.Response.FromString,
        )
    self.GetModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/GetModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.GetModelVersionRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.GetModelVersionRequest.Response.FromString,
        )
    self.CreateModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/CreateModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.SetModelVersion.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetModelVersion.Response.FromString,
        )
    self.UpdateModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/UpdateModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.SetModelVersion.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetModelVersion.Response.FromString,
        )
    self.SetLockModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/SetLockModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.SetLockModelVersionRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetLockModelVersionRequest.Response.FromString,
        )
    self.DeleteModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/DeleteModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.DeleteModelVersionRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.DeleteModelVersionRequest.Response.FromString,
        )
    self.getUrlForArtifact = channel.unary_unary(
        '/ai.verta.registry.RegistryService/getUrlForArtifact',
        request_serializer=registry_dot_RegistryService__pb2.GetUrlForArtifact.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.GetUrlForArtifact.Response.FromString,
        )
    self.commitArtifactPart = channel.unary_unary(
        '/ai.verta.registry.RegistryService/commitArtifactPart',
        request_serializer=registry_dot_RegistryService__pb2.CommitArtifactPart.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.CommitArtifactPart.Response.FromString,
        )
    self.getCommittedArtifactParts = channel.unary_unary(
        '/ai.verta.registry.RegistryService/getCommittedArtifactParts',
        request_serializer=registry_dot_RegistryService__pb2.GetCommittedArtifactParts.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.GetCommittedArtifactParts.Response.FromString,
        )
    self.commitMultipartArtifact = channel.unary_unary(
        '/ai.verta.registry.RegistryService/commitMultipartArtifact',
        request_serializer=registry_dot_RegistryService__pb2.CommitMultipartArtifact.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.CommitMultipartArtifact.Response.FromString,
        )
    self.logDatasetsInModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/logDatasetsInModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.LogDatasetsInModelVersion.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.LogDatasetsInModelVersion.Response.FromString,
        )
    self.logCodeBlobInModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/logCodeBlobInModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.LogCodeBlobInModelVersion.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.LogCodeBlobInModelVersion.Response.FromString,
        )
    self.logAttributesInModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/logAttributesInModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.LogAttributesInModelVersion.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.LogAttributesInModelVersion.Response.FromString,
        )
    self.logDockerMetadataInModelVersion = channel.unary_unary(
        '/ai.verta.registry.RegistryService/logDockerMetadataInModelVersion',
        request_serializer=registry_dot_RegistryService__pb2.LogDockerMetadataInModelVersion.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.LogDockerMetadataInModelVersion.Response.FromString,
        )
    self.GetExternalDeployment = channel.unary_unary(
        '/ai.verta.registry.RegistryService/GetExternalDeployment',
        request_serializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.Response.FromString,
        )
    self.CreateExternalDeployment = channel.unary_unary(
        '/ai.verta.registry.RegistryService/CreateExternalDeployment',
        request_serializer=registry_dot_RegistryService__pb2.ExternalDeployment.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.Response.FromString,
        )
    self.UpdateExternalDeployment = channel.unary_unary(
        '/ai.verta.registry.RegistryService/UpdateExternalDeployment',
        request_serializer=registry_dot_RegistryService__pb2.ExternalDeployment.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.Response.FromString,
        )
    self.DeleteExternalDeployment = channel.unary_unary(
        '/ai.verta.registry.RegistryService/DeleteExternalDeployment',
        request_serializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.Empty.FromString,
        )
    self.FindChecklistItemValues = channel.unary_unary(
        '/ai.verta.registry.RegistryService/FindChecklistItemValues',
        request_serializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.Response.FromString,
        )
    self.GetChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.RegistryService/GetChecklistItemValue',
        request_serializer=registry_dot_RegistryService__pb2.GetChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.GetChecklistItemValueRequest.Response.FromString,
        )
    self.CreateChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.RegistryService/CreateChecklistItemValue',
        request_serializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.Response.FromString,
        )
    self.UpdateChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.RegistryService/UpdateChecklistItemValue',
        request_serializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.Response.FromString,
        )
    self.DeleteChecklistItemValue = channel.unary_unary(
        '/ai.verta.registry.RegistryService/DeleteChecklistItemValue',
        request_serializer=registry_dot_RegistryService__pb2.DeleteChecklistItemValueRequest.SerializeToString,
        response_deserializer=registry_dot_RegistryService__pb2.DeleteChecklistItemValueRequest.Response.FromString,
        )


class RegistryServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FindRegisteredModel(self, request, context):
    """CRUD for RegisteredModel
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRegisteredModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRegisteredModelCount(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateRegisteredModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRegisteredModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteRegisteredModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindModelVersion(self, request, context):
    """CRUD for Model Version
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetLockModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUrlForArtifact(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def commitArtifactPart(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCommittedArtifactParts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def commitMultipartArtifact(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logDatasetsInModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logCodeBlobInModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logAttributesInModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def logDockerMetadataInModelVersion(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExternalDeployment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateExternalDeployment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateExternalDeployment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteExternalDeployment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindChecklistItemValues(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteChecklistItemValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RegistryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FindRegisteredModel': grpc.unary_unary_rpc_method_handler(
          servicer.FindRegisteredModel,
          request_deserializer=registry_dot_RegistryService__pb2.FindRegisteredModelRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.FindRegisteredModelRequest.Response.SerializeToString,
      ),
      'GetRegisteredModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetRegisteredModel,
          request_deserializer=registry_dot_RegistryService__pb2.GetRegisteredModelRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.GetRegisteredModelRequest.Response.SerializeToString,
      ),
      'GetRegisteredModelCount': grpc.unary_unary_rpc_method_handler(
          servicer.GetRegisteredModelCount,
          request_deserializer=registry_dot_RegistryService__pb2.GetRegisteredModelCountRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.GetRegisteredModelCountRequest.Response.SerializeToString,
      ),
      'CreateRegisteredModel': grpc.unary_unary_rpc_method_handler(
          servicer.CreateRegisteredModel,
          request_deserializer=registry_dot_RegistryService__pb2.SetRegisteredModel.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetRegisteredModel.Response.SerializeToString,
      ),
      'UpdateRegisteredModel': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRegisteredModel,
          request_deserializer=registry_dot_RegistryService__pb2.SetRegisteredModel.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetRegisteredModel.Response.SerializeToString,
      ),
      'DeleteRegisteredModel': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteRegisteredModel,
          request_deserializer=registry_dot_RegistryService__pb2.DeleteRegisteredModelRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.DeleteRegisteredModelRequest.Response.SerializeToString,
      ),
      'FindModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.FindModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.FindModelVersionRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.FindModelVersionRequest.Response.SerializeToString,
      ),
      'GetModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.GetModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.GetModelVersionRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.GetModelVersionRequest.Response.SerializeToString,
      ),
      'CreateModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.CreateModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.SetModelVersion.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetModelVersion.Response.SerializeToString,
      ),
      'UpdateModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.SetModelVersion.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetModelVersion.Response.SerializeToString,
      ),
      'SetLockModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.SetLockModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.SetLockModelVersionRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetLockModelVersionRequest.Response.SerializeToString,
      ),
      'DeleteModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.DeleteModelVersionRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.DeleteModelVersionRequest.Response.SerializeToString,
      ),
      'getUrlForArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.getUrlForArtifact,
          request_deserializer=registry_dot_RegistryService__pb2.GetUrlForArtifact.FromString,
          response_serializer=registry_dot_RegistryService__pb2.GetUrlForArtifact.Response.SerializeToString,
      ),
      'commitArtifactPart': grpc.unary_unary_rpc_method_handler(
          servicer.commitArtifactPart,
          request_deserializer=registry_dot_RegistryService__pb2.CommitArtifactPart.FromString,
          response_serializer=registry_dot_RegistryService__pb2.CommitArtifactPart.Response.SerializeToString,
      ),
      'getCommittedArtifactParts': grpc.unary_unary_rpc_method_handler(
          servicer.getCommittedArtifactParts,
          request_deserializer=registry_dot_RegistryService__pb2.GetCommittedArtifactParts.FromString,
          response_serializer=registry_dot_RegistryService__pb2.GetCommittedArtifactParts.Response.SerializeToString,
      ),
      'commitMultipartArtifact': grpc.unary_unary_rpc_method_handler(
          servicer.commitMultipartArtifact,
          request_deserializer=registry_dot_RegistryService__pb2.CommitMultipartArtifact.FromString,
          response_serializer=registry_dot_RegistryService__pb2.CommitMultipartArtifact.Response.SerializeToString,
      ),
      'logDatasetsInModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.logDatasetsInModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.LogDatasetsInModelVersion.FromString,
          response_serializer=registry_dot_RegistryService__pb2.LogDatasetsInModelVersion.Response.SerializeToString,
      ),
      'logCodeBlobInModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.logCodeBlobInModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.LogCodeBlobInModelVersion.FromString,
          response_serializer=registry_dot_RegistryService__pb2.LogCodeBlobInModelVersion.Response.SerializeToString,
      ),
      'logAttributesInModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.logAttributesInModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.LogAttributesInModelVersion.FromString,
          response_serializer=registry_dot_RegistryService__pb2.LogAttributesInModelVersion.Response.SerializeToString,
      ),
      'logDockerMetadataInModelVersion': grpc.unary_unary_rpc_method_handler(
          servicer.logDockerMetadataInModelVersion,
          request_deserializer=registry_dot_RegistryService__pb2.LogDockerMetadataInModelVersion.FromString,
          response_serializer=registry_dot_RegistryService__pb2.LogDockerMetadataInModelVersion.Response.SerializeToString,
      ),
      'GetExternalDeployment': grpc.unary_unary_rpc_method_handler(
          servicer.GetExternalDeployment,
          request_deserializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.Response.SerializeToString,
      ),
      'CreateExternalDeployment': grpc.unary_unary_rpc_method_handler(
          servicer.CreateExternalDeployment,
          request_deserializer=registry_dot_RegistryService__pb2.ExternalDeployment.FromString,
          response_serializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.Response.SerializeToString,
      ),
      'UpdateExternalDeployment': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateExternalDeployment,
          request_deserializer=registry_dot_RegistryService__pb2.ExternalDeployment.FromString,
          response_serializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.Response.SerializeToString,
      ),
      'DeleteExternalDeployment': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteExternalDeployment,
          request_deserializer=registry_dot_RegistryService__pb2.ExternalDeploymentRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.Empty.SerializeToString,
      ),
      'FindChecklistItemValues': grpc.unary_unary_rpc_method_handler(
          servicer.FindChecklistItemValues,
          request_deserializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.FindChecklistItemValueRequest.Response.SerializeToString,
      ),
      'GetChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.GetChecklistItemValue,
          request_deserializer=registry_dot_RegistryService__pb2.GetChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.GetChecklistItemValueRequest.Response.SerializeToString,
      ),
      'CreateChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.CreateChecklistItemValue,
          request_deserializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.Response.SerializeToString,
      ),
      'UpdateChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateChecklistItemValue,
          request_deserializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.SetChecklistItemValueRequest.Response.SerializeToString,
      ),
      'DeleteChecklistItemValue': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteChecklistItemValue,
          request_deserializer=registry_dot_RegistryService__pb2.DeleteChecklistItemValueRequest.FromString,
          response_serializer=registry_dot_RegistryService__pb2.DeleteChecklistItemValueRequest.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.registry.RegistryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
