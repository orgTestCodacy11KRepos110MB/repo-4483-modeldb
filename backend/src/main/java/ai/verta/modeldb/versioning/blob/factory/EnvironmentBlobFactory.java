package ai.verta.modeldb.versioning.blob.factory;

import static ai.verta.modeldb.versioning.blob.container.EnvironmentContainer.DOCKER_ENV_TYPE;
import static ai.verta.modeldb.versioning.blob.container.EnvironmentContainer.PYTHON_ENV_TYPE;

import ai.verta.modeldb.entities.environment.EnvironmentBlobEntity;
import ai.verta.modeldb.entities.environment.EnvironmentCommandLineEntity;
import ai.verta.modeldb.entities.environment.EnvironmentVariablesEntity;
import ai.verta.modeldb.entities.environment.PythonEnvironmentRequirementBlobEntity;
import ai.verta.modeldb.entities.versioning.InternalFolderElementEntity;
import ai.verta.modeldb.versioning.Blob;
import ai.verta.modeldb.versioning.EnvironmentBlob;
import ai.verta.modeldb.versioning.PythonEnvironmentBlob;
import org.hibernate.Session;

public class EnvironmentBlobFactory extends BlobFactory {
  EnvironmentBlobFactory(InternalFolderElementEntity internalFolderElementEntity) {
    super(
        internalFolderElementEntity.getElement_type(),
        internalFolderElementEntity.getElement_sha());
  }

  @Override
  public Blob getBlob(Session session) {
    var environmentBlobBuilder = EnvironmentBlob.newBuilder();
    var environmentBlobEntity = session.get(EnvironmentBlobEntity.class, getElementSha());
    switch (environmentBlobEntity.getEnvironment_type()) {
      case PYTHON_ENV_TYPE:
        var pythonEnvironmentBlobBuilder = PythonEnvironmentBlob.newBuilder();
        var pythonEnvironmentBlobEntity = environmentBlobEntity.getPythonEnvironmentBlobEntity();
        pythonEnvironmentBlobBuilder.setVersion(pythonEnvironmentBlobEntity.getVersion());
        for (PythonEnvironmentRequirementBlobEntity pythonEnvironmentRequirementBlobEntity :
            pythonEnvironmentBlobEntity.getPythonEnvironmentRequirementBlobEntity()) {
          pythonEnvironmentRequirementBlobEntity.toProto(pythonEnvironmentBlobBuilder);
        }
        pythonEnvironmentBlobBuilder.setRawRequirements(
            pythonEnvironmentBlobEntity.getRaw_requirements());
        pythonEnvironmentBlobBuilder.setRawConstraints(
            pythonEnvironmentBlobEntity.getRaw_constraints());
        environmentBlobBuilder.setPython(pythonEnvironmentBlobBuilder);
        break;
      case DOCKER_ENV_TYPE:
        var dockerEnvironmentBlobBuilder =
            environmentBlobEntity.getDockerEnvironmentBlobEntity().toProto();
        environmentBlobBuilder.setDocker(dockerEnvironmentBlobBuilder);
        break;
      default:
        // Do nothing
        break;
    }
    for (EnvironmentCommandLineEntity environmentCommandLineEntity :
        environmentBlobEntity.getEnvironmentCommandLineEntities()) {
      environmentBlobBuilder.addCommandLine(environmentCommandLineEntity.getCommand());
    }

    for (EnvironmentVariablesEntity environmentVariablesEntity :
        environmentBlobEntity.getEnvironmentVariablesEntities()) {
      environmentBlobBuilder.addEnvironmentVariables(environmentVariablesEntity.toProto());
    }
    return Blob.newBuilder().setEnvironment(environmentBlobBuilder).build();
  }
}
