package ai.verta.modeldb.configuration;

import ai.verta.modeldb.artifactStore.storageservice.ArtifactStoreService;
import ai.verta.modeldb.artifactStore.storageservice.nfs.FileStorageProperties;
import ai.verta.modeldb.artifactStore.storageservice.nfs.NFSController;
import ai.verta.modeldb.artifactStore.storageservice.nfs.NFSService;
import ai.verta.modeldb.artifactStore.storageservice.s3.S3Controller;
import ai.verta.modeldb.artifactStore.storageservice.s3.S3Service;
import ai.verta.modeldb.common.configuration.AppContext;
import ai.verta.modeldb.common.exceptions.ModelDBException;
import ai.verta.modeldb.config.MDBConfig;
import java.io.IOException;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ArtifactStoreInitBeans {

  private static final Logger LOGGER = LogManager.getLogger(ArtifactStoreInitBeans.class);

  @Bean
  public ArtifactStoreService artifactStoreService(MDBConfig config, AppContext appContext)
      throws IOException {

    final var artifactStoreConfig = config.artifactStoreConfig;
    if (artifactStoreConfig.isEnabled()) {
      //
      // TODO: This is backwards, these values can be extracted from the environment or injected
      // using profiles instead
      // ------------- Start Initialize Cloud storage base on configuration ------------------
      ArtifactStoreService artifactStoreService;

      if (artifactStoreConfig.getArtifactEndpoint() != null) {
        System.getProperties()
            .put(
                "artifactEndpoint.storeArtifact",
                artifactStoreConfig.getArtifactEndpoint().getStoreArtifact());
        System.getProperties()
            .put(
                "artifactEndpoint.getArtifact",
                artifactStoreConfig.getArtifactEndpoint().getGetArtifact());
      }

      if (artifactStoreConfig.getArtifactStoreType().equals("NFS")
          && artifactStoreConfig.getNFS() != null
          && artifactStoreConfig.getNFS().getArtifactEndpoint() != null) {
        System.getProperties()
            .put(
                "artifactEndpoint.storeArtifact",
                artifactStoreConfig.getNFS().getArtifactEndpoint().getStoreArtifact());
        System.getProperties()
            .put(
                "artifactEndpoint.getArtifact",
                artifactStoreConfig.getNFS().getArtifactEndpoint().getGetArtifact());
      }

      switch (artifactStoreConfig.getArtifactStoreType()) {
        case "S3":
          if (!artifactStoreConfig.S3.getS3presignedURLEnabled()) {
            appContext.registerBean("s3Controller", S3Controller.class);
          }
          artifactStoreService = new S3Service(artifactStoreConfig.S3.getCloudBucketName());
          break;
        case "NFS":
          appContext.registerBean("nfsController", NFSController.class);
          String rootDir = artifactStoreConfig.getNFS().getNfsRootPath();
          LOGGER.trace("NFS server root path {}", rootDir);
          final var props = new FileStorageProperties();
          props.setUploadDir(rootDir);
          artifactStoreService = new NFSService(props);
          break;
        default:
          throw new ModelDBException("Configure valid artifact store name in config.yaml file.");
      }
      // ------------- Finish Initialize Cloud storage base on configuration ------------------

      LOGGER.info(
          "ArtifactStore service initialized and resolved storage dependency before server start");
      return artifactStoreService;
    } else {
      LOGGER.info("Artifact store service is disabled.");
      return null;
    }
  }
}
