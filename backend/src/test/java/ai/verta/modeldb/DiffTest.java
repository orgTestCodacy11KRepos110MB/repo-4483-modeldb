package ai.verta.modeldb;

import static ai.verta.modeldb.CommitTest.getDatasetBlobFromPath;
import static org.junit.Assert.*;

import ai.verta.modeldb.common.CommonUtils;
import ai.verta.modeldb.versioning.Blob;
import ai.verta.modeldb.versioning.BlobDiff;
import ai.verta.modeldb.versioning.BlobExpanded;
import ai.verta.modeldb.versioning.CodeDiff;
import ai.verta.modeldb.versioning.Commit;
import ai.verta.modeldb.versioning.ComputeRepositoryDiffRequest;
import ai.verta.modeldb.versioning.ConfigDiff;
import ai.verta.modeldb.versioning.ContinuousHyperparameterSetConfigBlob;
import ai.verta.modeldb.versioning.CreateCommitRequest;
import ai.verta.modeldb.versioning.DeleteBranchRequest;
import ai.verta.modeldb.versioning.DeleteCommitRequest;
import ai.verta.modeldb.versioning.DeleteRepositoryRequest;
import ai.verta.modeldb.versioning.DiffStatusEnum.DiffStatus;
import ai.verta.modeldb.versioning.EnvironmentBlob;
import ai.verta.modeldb.versioning.EnvironmentVariablesBlob;
import ai.verta.modeldb.versioning.GetBranchRequest;
import ai.verta.modeldb.versioning.GitCodeBlob;
import ai.verta.modeldb.versioning.GitCodeDiff;
import ai.verta.modeldb.versioning.HyperparameterConfigBlob;
import ai.verta.modeldb.versioning.HyperparameterConfigDiff;
import ai.verta.modeldb.versioning.HyperparameterConfigDiff.Builder;
import ai.verta.modeldb.versioning.HyperparameterSetConfigBlob;
import ai.verta.modeldb.versioning.HyperparameterSetConfigDiff;
import ai.verta.modeldb.versioning.HyperparameterValuesConfigBlob;
import ai.verta.modeldb.versioning.NotebookCodeDiff;
import ai.verta.modeldb.versioning.PathDatasetComponentDiff;
import ai.verta.modeldb.versioning.PythonEnvironmentBlob;
import ai.verta.modeldb.versioning.PythonRequirementEnvironmentBlob;
import ai.verta.modeldb.versioning.Repository;
import ai.verta.modeldb.versioning.RepositoryIdentification;
import ai.verta.modeldb.versioning.SetBranchRequest;
import ai.verta.modeldb.versioning.SetRepository;
import ai.verta.modeldb.versioning.VersionEnvironmentBlob;
import com.google.protobuf.InvalidProtocolBufferException;
import io.grpc.Status;
import io.grpc.StatusRuntimeException;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collection;
import java.util.Collections;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.FixMethodOrder;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.MethodSorters;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

/**
 * Tests diffs after commit creation with diff or blob description and checks resulting diff. Tests
 * 2 modified cases: same type and different type.
 */
@RunWith(Parameterized.class)
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class DiffTest extends TestsInit {

  private static final Logger LOGGER = LogManager.getLogger(DiffTest.class);
  private static final String FIRST_NAME = "train.json";
  private static final String OTHER_NAME = "environment.json";
  private static final boolean USE_SAME_NAMES = false; // TODO: set to true after fixing VR-3688
  private static final String SECOND_NAME = USE_SAME_NAMES ? FIRST_NAME : OTHER_NAME;

  private static Repository repository;
  private static Commit parentCommit;

  private final int blobType;
  private final int commitType;

  // 1. blob type: 0 -- dataset path, 1 -- config, 2 -- python environment, 3 -- Git Notebook Code
  // 2. commit type -- 0 -- blob, 1 -- diff
  @Parameters
  public static Collection<Object[]> data() {
    return Arrays.asList(new Object[][] {{0, 0}, {1, 1}, {2, 0}, {3, 1}});
  }

  public DiffTest(int blobType, int commitType) {
    this.blobType = blobType;
    this.commitType = commitType;
  }

  @Before
  public void createEntities() {
    // Create all entities
    createRepositoryEntities();
  }

  @After
  public void removeEntities() {
    for (Repository repo : new Repository[] {repository}) {
      DeleteRepositoryRequest deleteRepository =
          DeleteRepositoryRequest.newBuilder()
              .setRepositoryId(RepositoryIdentification.newBuilder().setRepoId(repo.getId()))
              .build();
      DeleteRepositoryRequest.Response response =
          versioningServiceBlockingStub.deleteRepository(deleteRepository);
      assertTrue("Repository not delete", response.getStatus());
    }

    repository = null;
  }

  private static void createRepositoryEntities() {
    String repoName = "Repo-" + new Date().getTime();
    SetRepository setRepository = RepositoryTest.getSetRepositoryRequest(repoName);
    repository = versioningServiceBlockingStub.createRepository(setRepository).getRepository();
    LOGGER.info("Repository created successfully");
    assertEquals(
        "Repository name not match with expected Repository name", repoName, repository.getName());

    GetBranchRequest getBranchRequest =
        GetBranchRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setBranch(ModelDBConstants.MASTER_BRANCH)
            .build();
    GetBranchRequest.Response getBranchResponse =
        versioningServiceBlockingStub.getBranch(getBranchRequest);
    parentCommit = getBranchResponse.getCommit();
  }

  @Test
  public void computeRepositoryDiffTest() throws InvalidProtocolBufferException {
    LOGGER.info("Compute repository diff test start................................");

    BlobExpanded[] blobExpandedArray;
    BlobDiff[] blobDiffsArray;
    if (commitType == 0) {
      blobExpandedArray = createBlobs(blobType);
      blobDiffsArray = null;
    } else {
      blobExpandedArray = null;
      blobDiffsArray = createDiffs(blobType);
    }

    CreateCommitRequest.Builder createCommitRequestBuilder =
        CreateCommitRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommit(createCommit(parentCommit.getCommitSha()));
    CreateCommitRequest createCommitRequest;
    if (commitType == 0) {
      LinkedList<BlobExpanded> blobsA = new LinkedList<>();
      blobsA.add(blobExpandedArray[0]);
      blobsA.add(blobExpandedArray[1]);
      blobsA.add(blobExpandedArray[2]);
      blobsA.add(blobExpandedArray[3]);
      createCommitRequest = createCommitRequestBuilder.addAllBlobs(blobsA).build();
    } else {
      createCommitRequest =
          createCommitRequestBuilder
              .setCommitBase(parentCommit.getCommitSha())
              .addDiffs(blobDiffsArray[0])
              .addDiffs(blobDiffsArray[1])
              .addDiffs(blobDiffsArray[2])
              .addDiffs(blobDiffsArray[3])
              .build();
    }

    CreateCommitRequest.Response commitResponse =
        versioningServiceBlockingStub.createCommit(createCommitRequest);
    Commit commitA = commitResponse.getCommit();

    createCommitRequestBuilder =
        CreateCommitRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommit(createCommit(commitA.getCommitSha()));
    if (commitType == 0) {
      blobExpandedArray[2] = modifiedBlobExpanded(blobType);
    } else {
      blobDiffsArray[0] = deleteBlobDiff1(blobType);
      blobDiffsArray[3] = deleteBlobDiff4(blobType);
      blobDiffsArray[2] = modifiedBlobDiff(blobType);
    }
    if (commitType == 0) {
      LinkedList<BlobExpanded> blobsB = new LinkedList<>();
      blobsB.add(blobExpandedArray[1]);
      blobsB.add(blobExpandedArray[2]);
      blobsB.add(blobExpandedArray[4]);
      createCommitRequest = createCommitRequestBuilder.addAllBlobs(blobsB).build();
    } else {
      createCommitRequest =
          createCommitRequestBuilder
              .setCommitBase(commitA.getCommitSha())
              .addDiffs(blobDiffsArray[0])
              .addDiffs(blobDiffsArray[2])
              .addDiffs(blobDiffsArray[3])
              .addDiffs(blobDiffsArray[4])
              .build();
    }

    commitResponse = versioningServiceBlockingStub.createCommit(createCommitRequest);
    Commit commitB = commitResponse.getCommit();

    ComputeRepositoryDiffRequest repositoryDiffRequest =
        ComputeRepositoryDiffRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommitA(commitA.getCommitSha())
            .setCommitB(commitB.getCommitSha())
            .build();
    ComputeRepositoryDiffRequest.Response repositoryDiffResponse =
        versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
    LOGGER.info("Diff Response: {}", CommonUtils.getStringFromProtoObject(repositoryDiffResponse));
    LOGGER.info("Diff Response: {}", repositoryDiffResponse);
    List<BlobDiff> blobDiffs = repositoryDiffResponse.getDiffsList();
    final boolean differentTypesModified = blobType > 1;
    final int expectedCount = differentTypesModified ? 5 : 4;
    Assert.assertEquals(
        "blob count not match with expected blob count", expectedCount, blobDiffs.size());
    Map<String, BlobDiff> result =
        blobDiffs.stream()
            .collect(
                Collectors.toMap(
                    blobDiff -> String.join("#", blobDiff.getLocationList()) + blobDiff.getStatus(),
                    blobDiff -> blobDiff));
    BlobDiff blobDiff = result.get("maths/algebra" + DiffStatus.ADDED);
    Assert.assertNotNull(blobDiff);
    BlobDiff blobDiff1 = result.get("modeldb.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff1);
    BlobDiff blobDiff2 = result.get("modeldb#march#environment#train.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff2);
    final BlobDiff blobDiff3;
    if (differentTypesModified) {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.ADDED);
      Assert.assertNotNull(blobDiff3);
      final BlobDiff blobDiff3Deleted =
          result.get("modeldb#blob#march#blob.json" + DiffStatus.DELETED);
      Assert.assertNotNull(blobDiff3Deleted);
    } else {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.MODIFIED);
      Assert.assertNotNull(blobDiff3);
    }

    for (Commit commit : new Commit[] {commitB, commitA}) {
      DeleteCommitRequest deleteCommitRequest =
          DeleteCommitRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitSha(commit.getCommitSha())
              .build();
      versioningServiceBlockingStub.deleteCommit(deleteCommitRequest);
    }

    LOGGER.info("Compute repository diff test end................................");
  }

  @Test
  public void computeRepositoryDiffWithBranchTest() throws InvalidProtocolBufferException {
    LOGGER.info("Compute repository diff with branch test start................................");

    BlobExpanded[] blobExpandedArray;
    BlobDiff[] blobDiffsArray;
    if (commitType == 0) {
      blobExpandedArray = createBlobs(blobType);
      blobDiffsArray = null;
    } else {
      blobExpandedArray = null;
      blobDiffsArray = createDiffs(blobType);
    }

    CreateCommitRequest.Builder createCommitRequestBuilder =
        CreateCommitRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommit(createCommit(parentCommit.getCommitSha()));
    CreateCommitRequest createCommitRequest;
    if (commitType == 0) {
      LinkedList<BlobExpanded> blobsA = new LinkedList<>();
      blobsA.add(blobExpandedArray[0]);
      blobsA.add(blobExpandedArray[1]);
      blobsA.add(blobExpandedArray[2]);
      blobsA.add(blobExpandedArray[3]);
      createCommitRequest = createCommitRequestBuilder.addAllBlobs(blobsA).build();
    } else {
      createCommitRequest =
          createCommitRequestBuilder
              .setCommitBase(parentCommit.getCommitSha())
              .addDiffs(blobDiffsArray[0])
              .addDiffs(blobDiffsArray[1])
              .addDiffs(blobDiffsArray[2])
              .addDiffs(blobDiffsArray[3])
              .build();
    }

    CreateCommitRequest.Response commitResponse =
        versioningServiceBlockingStub.createCommit(createCommitRequest);
    Commit commitA = commitResponse.getCommit();

    // Create branch 1
    String branchA = "branch-1-" + new Date().getTime();
    createBranch(repository.getId(), branchA, commitA.getCommitSha());

    createCommitRequestBuilder =
        CreateCommitRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommit(createCommit(commitA.getCommitSha()));
    if (commitType == 0) {
      blobExpandedArray[2] = modifiedBlobExpanded(blobType);
    } else {
      blobDiffsArray[0] = deleteBlobDiff1(blobType);
      blobDiffsArray[3] = deleteBlobDiff4(blobType);
      blobDiffsArray[2] = modifiedBlobDiff(blobType);
    }
    if (commitType == 0) {
      LinkedList<BlobExpanded> blobsB = new LinkedList<>();
      blobsB.add(blobExpandedArray[1]);
      blobsB.add(blobExpandedArray[2]);
      blobsB.add(blobExpandedArray[4]);
      createCommitRequest = createCommitRequestBuilder.addAllBlobs(blobsB).build();
    } else {
      createCommitRequest =
          createCommitRequestBuilder
              .setCommitBase(commitA.getCommitSha())
              .addDiffs(blobDiffsArray[0])
              .addDiffs(blobDiffsArray[2])
              .addDiffs(blobDiffsArray[3])
              .addDiffs(blobDiffsArray[4])
              .build();
    }

    commitResponse = versioningServiceBlockingStub.createCommit(createCommitRequest);
    Commit commitB = commitResponse.getCommit();

    // Create branch 2
    String branchB = "branch-2-" + new Date().getTime();
    createBranch(repository.getId(), branchB, commitB.getCommitSha());

    ComputeRepositoryDiffRequest repositoryDiffRequest =
        ComputeRepositoryDiffRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setBranchA(branchA)
            .setBranchB(branchB)
            .build();
    ComputeRepositoryDiffRequest.Response repositoryDiffResponse =
        versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
    LOGGER.info("Diff Response: {}", CommonUtils.getStringFromProtoObject(repositoryDiffResponse));
    LOGGER.info("Diff Response: {}", repositoryDiffResponse);
    List<BlobDiff> blobDiffs = repositoryDiffResponse.getDiffsList();
    final boolean differentTypesModified = blobType > 1;
    final int expectedCount = differentTypesModified ? 5 : 4;
    Assert.assertEquals(
        "blob count not match with expected blob count", expectedCount, blobDiffs.size());
    Map<String, BlobDiff> result =
        blobDiffs.stream()
            .collect(
                Collectors.toMap(
                    blobDiff -> String.join("#", blobDiff.getLocationList()) + blobDiff.getStatus(),
                    blobDiff -> blobDiff));
    BlobDiff blobDiff = result.get("maths/algebra" + DiffStatus.ADDED);
    Assert.assertNotNull(blobDiff);
    BlobDiff blobDiff1 = result.get("modeldb.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff1);
    BlobDiff blobDiff2 = result.get("modeldb#march#environment#train.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff2);
    final BlobDiff blobDiff3;
    if (differentTypesModified) {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.ADDED);
      Assert.assertNotNull(blobDiff3);
      final BlobDiff blobDiff3Deleted =
          result.get("modeldb#blob#march#blob.json" + DiffStatus.DELETED);
      Assert.assertNotNull(blobDiff3Deleted);
    } else {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.MODIFIED);
      Assert.assertNotNull(blobDiff3);
    }

    for (String branch : new String[] {branchA, branchB}) {
      DeleteBranchRequest deleteBranchRequest =
          DeleteBranchRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setBranch(branch)
              .build();
      versioningServiceBlockingStub.deleteBranch(deleteBranchRequest);
    }

    for (Commit commit : new Commit[] {commitB, commitA}) {
      DeleteCommitRequest deleteCommitRequest =
          DeleteCommitRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitSha(commit.getCommitSha())
              .build();
      versioningServiceBlockingStub.deleteCommit(deleteCommitRequest);
    }

    LOGGER.info("Compute repository diff with branch test end................................");
  }

  @Test
  public void computeRepositoryDiffWithOneBranchOneCommitTest()
      throws InvalidProtocolBufferException {
    LOGGER.info("Compute repository diff with one branch one commit test start...");

    BlobExpanded[] blobExpandedArray;
    BlobDiff[] blobDiffsArray;
    if (commitType == 0) {
      blobExpandedArray = createBlobs(blobType);
      blobDiffsArray = null;
    } else {
      blobExpandedArray = null;
      blobDiffsArray = createDiffs(blobType);
    }

    CreateCommitRequest.Builder createCommitRequestBuilder =
        CreateCommitRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommit(createCommit(parentCommit.getCommitSha()));
    CreateCommitRequest createCommitRequest;
    if (commitType == 0) {
      LinkedList<BlobExpanded> blobsA = new LinkedList<>();
      blobsA.add(blobExpandedArray[0]);
      blobsA.add(blobExpandedArray[1]);
      blobsA.add(blobExpandedArray[2]);
      blobsA.add(blobExpandedArray[3]);
      createCommitRequest = createCommitRequestBuilder.addAllBlobs(blobsA).build();
    } else {
      createCommitRequest =
          createCommitRequestBuilder
              .setCommitBase(parentCommit.getCommitSha())
              .addDiffs(blobDiffsArray[0])
              .addDiffs(blobDiffsArray[1])
              .addDiffs(blobDiffsArray[2])
              .addDiffs(blobDiffsArray[3])
              .build();
    }

    CreateCommitRequest.Response commitResponse =
        versioningServiceBlockingStub.createCommit(createCommitRequest);
    Commit commitA = commitResponse.getCommit();

    // Create branch 1
    String branchA = "branch-1-" + new Date().getTime();
    createBranch(repository.getId(), branchA, commitA.getCommitSha());

    createCommitRequestBuilder =
        CreateCommitRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommit(createCommit(commitA.getCommitSha()));
    if (commitType == 0) {
      blobExpandedArray[2] = modifiedBlobExpanded(blobType);
    } else {
      blobDiffsArray[0] = deleteBlobDiff1(blobType);
      blobDiffsArray[3] = deleteBlobDiff4(blobType);
      blobDiffsArray[2] = modifiedBlobDiff(blobType);
    }
    if (commitType == 0) {
      LinkedList<BlobExpanded> blobsB = new LinkedList<>();
      blobsB.add(blobExpandedArray[1]);
      blobsB.add(blobExpandedArray[2]);
      blobsB.add(blobExpandedArray[4]);
      createCommitRequest = createCommitRequestBuilder.addAllBlobs(blobsB).build();
    } else {
      createCommitRequest =
          createCommitRequestBuilder
              .setCommitBase(commitA.getCommitSha())
              .addDiffs(blobDiffsArray[0])
              .addDiffs(blobDiffsArray[2])
              .addDiffs(blobDiffsArray[3])
              .addDiffs(blobDiffsArray[4])
              .build();
    }

    commitResponse = versioningServiceBlockingStub.createCommit(createCommitRequest);
    Commit commitB = commitResponse.getCommit();

    // Create branch 2
    String branchB = "branch-2-" + new Date().getTime();
    createBranch(repository.getId(), branchB, commitB.getCommitSha());

    // CA - 1, BA - 1, CB - 1, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitA(commitA.getCommitSha())
              .setBranchA(branchA)
              .setCommitB(commitB.getCommitSha())
              .setBranchB(branchB)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 1, CB - 1, BB - 0
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitA(commitA.getCommitSha())
              .setBranchA(branchA)
              .setCommitB(commitB.getCommitSha())
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 1, CB - 0, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitA(commitA.getCommitSha())
              .setBranchA(branchA)
              .setBranchB(branchB)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 1, CB - 0, BB - 0
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitA(commitA.getCommitSha())
              .setBranchA(branchA)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 0, CB - 1, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitA(commitA.getCommitSha())
              .setCommitB(commitB.getCommitSha())
              .setBranchB(branchB)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 0, CB - 0, BB - 0
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitA(commitA.getCommitSha())
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 0, BA - 1, CB - 1, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setBranchA(branchA)
              .setCommitB(commitB.getCommitSha())
              .setBranchB(branchB)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 0, BA - 1, CB - 0, BB - 0
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setBranchA(branchA)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 0, BA - 0, CB - 1, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitB(commitB.getCommitSha())
              .setBranchB(branchB)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 0, BA - 0, CB - 1, BB - 0
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitB(commitB.getCommitSha())
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 0, BA - 0, CB - 0, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setBranchB(branchB)
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 1, CB - 1, BB - 1
    try {
      ComputeRepositoryDiffRequest repositoryDiffRequest =
          ComputeRepositoryDiffRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .build();
      versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
      fail();
    } catch (StatusRuntimeException ex) {
      Status status = Status.fromThrowable(ex);
      LOGGER.warn("Error Code : " + status.getCode() + " Description : " + status.getDescription());
      assertEquals(Status.INVALID_ARGUMENT.getCode(), status.getCode());
    }

    // CA - 1, BA - 0, CB - 1, BB - 0
    ComputeRepositoryDiffRequest repositoryDiffRequest =
        ComputeRepositoryDiffRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommitA(commitA.getCommitSha())
            .setCommitB(commitB.getCommitSha())
            .build();
    ComputeRepositoryDiffRequest.Response repositoryDiffResponse =
        versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
    LOGGER.info("Diff Response: {}", CommonUtils.getStringFromProtoObject(repositoryDiffResponse));
    LOGGER.info("Diff Response: {}", repositoryDiffResponse);
    List<BlobDiff> blobDiffs = repositoryDiffResponse.getDiffsList();
    boolean differentTypesModified = blobType > 1;
    int expectedCount = differentTypesModified ? 5 : 4;
    Assert.assertEquals(
        "blob count not match with expected blob count", expectedCount, blobDiffs.size());
    Map<String, BlobDiff> result =
        blobDiffs.stream()
            .collect(
                Collectors.toMap(
                    blobDiff -> String.join("#", blobDiff.getLocationList()) + blobDiff.getStatus(),
                    blobDiff -> blobDiff));
    BlobDiff blobDiff = result.get("maths/algebra" + DiffStatus.ADDED);
    Assert.assertNotNull(blobDiff);
    BlobDiff blobDiff1 = result.get("modeldb.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff1);
    BlobDiff blobDiff2 = result.get("modeldb#march#environment#train.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff2);
    BlobDiff blobDiff3;
    if (differentTypesModified) {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.ADDED);
      Assert.assertNotNull(blobDiff3);
      final BlobDiff blobDiff3Deleted =
          result.get("modeldb#blob#march#blob.json" + DiffStatus.DELETED);
      Assert.assertNotNull(blobDiff3Deleted);
    } else {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.MODIFIED);
      Assert.assertNotNull(blobDiff3);
    }

    // CA - 1, BA - 0, CB - 0, BB - 1
    repositoryDiffRequest =
        ComputeRepositoryDiffRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setCommitA(commitA.getCommitSha())
            .setBranchB(branchB)
            .build();
    repositoryDiffResponse =
        versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
    LOGGER.info("Diff Response: {}", CommonUtils.getStringFromProtoObject(repositoryDiffResponse));
    LOGGER.info("Diff Response: {}", repositoryDiffResponse);
    blobDiffs = repositoryDiffResponse.getDiffsList();
    differentTypesModified = blobType > 1;
    expectedCount = differentTypesModified ? 5 : 4;
    Assert.assertEquals(
        "blob count not match with expected blob count", expectedCount, blobDiffs.size());
    result =
        blobDiffs.stream()
            .collect(
                Collectors.toMap(
                    blobDiff111 ->
                        String.join("#", blobDiff111.getLocationList()) + blobDiff111.getStatus(),
                    blobDiff111 -> blobDiff111));
    blobDiff = result.get("maths/algebra" + DiffStatus.ADDED);
    Assert.assertNotNull(blobDiff);
    blobDiff1 = result.get("modeldb.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff1);
    blobDiff2 = result.get("modeldb#march#environment#train.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff2);
    if (differentTypesModified) {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.ADDED);
      Assert.assertNotNull(blobDiff3);
      final BlobDiff blobDiff3Deleted =
          result.get("modeldb#blob#march#blob.json" + DiffStatus.DELETED);
      Assert.assertNotNull(blobDiff3Deleted);
    } else {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.MODIFIED);
      Assert.assertNotNull(blobDiff3);
    }

    // CA - 0, BA - 1, CB - 1, BB - 0
    repositoryDiffRequest =
        ComputeRepositoryDiffRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setBranchA(branchA)
            .setCommitB(commitB.getCommitSha())
            .build();
    repositoryDiffResponse =
        versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
    LOGGER.info("Diff Response: {}", CommonUtils.getStringFromProtoObject(repositoryDiffResponse));
    LOGGER.info("Diff Response: {}", repositoryDiffResponse);
    blobDiffs = repositoryDiffResponse.getDiffsList();
    differentTypesModified = blobType > 1;
    expectedCount = differentTypesModified ? 5 : 4;
    Assert.assertEquals(
        "blob count not match with expected blob count", expectedCount, blobDiffs.size());
    result =
        blobDiffs.stream()
            .collect(
                Collectors.toMap(
                    blobDiff111 ->
                        String.join("#", blobDiff111.getLocationList()) + blobDiff111.getStatus(),
                    blobDiff111 -> blobDiff111));
    blobDiff = result.get("maths/algebra" + DiffStatus.ADDED);
    Assert.assertNotNull(blobDiff);
    blobDiff1 = result.get("modeldb.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff1);
    blobDiff2 = result.get("modeldb#march#environment#train.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff2);
    if (differentTypesModified) {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.ADDED);
      Assert.assertNotNull(blobDiff3);
      final BlobDiff blobDiff3Deleted =
          result.get("modeldb#blob#march#blob.json" + DiffStatus.DELETED);
      Assert.assertNotNull(blobDiff3Deleted);
    } else {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.MODIFIED);
      Assert.assertNotNull(blobDiff3);
    }

    // CA - 0, BA - 1, CB - 0, BB - 1
    repositoryDiffRequest =
        ComputeRepositoryDiffRequest.newBuilder()
            .setRepositoryId(
                RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
            .setBranchA(branchA)
            .setBranchB(branchB)
            .build();
    repositoryDiffResponse =
        versioningServiceBlockingStub.computeRepositoryDiff(repositoryDiffRequest);
    LOGGER.info("Diff Response: {}", CommonUtils.getStringFromProtoObject(repositoryDiffResponse));
    LOGGER.info("Diff Response: {}", repositoryDiffResponse);
    blobDiffs = repositoryDiffResponse.getDiffsList();
    differentTypesModified = blobType > 1;
    expectedCount = differentTypesModified ? 5 : 4;
    Assert.assertEquals(
        "blob count not match with expected blob count", expectedCount, blobDiffs.size());
    result =
        blobDiffs.stream()
            .collect(
                Collectors.toMap(
                    blobDiff111 ->
                        String.join("#", blobDiff111.getLocationList()) + blobDiff111.getStatus(),
                    blobDiff111 -> blobDiff111));
    blobDiff = result.get("maths/algebra" + DiffStatus.ADDED);
    Assert.assertNotNull(blobDiff);
    blobDiff1 = result.get("modeldb.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff1);
    blobDiff2 = result.get("modeldb#march#environment#train.json" + DiffStatus.DELETED);
    Assert.assertNotNull(blobDiff2);
    if (differentTypesModified) {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.ADDED);
      Assert.assertNotNull(blobDiff3);
      final BlobDiff blobDiff3Deleted =
          result.get("modeldb#blob#march#blob.json" + DiffStatus.DELETED);
      Assert.assertNotNull(blobDiff3Deleted);
    } else {
      blobDiff3 = result.get("modeldb#blob#march#blob.json" + DiffStatus.MODIFIED);
      Assert.assertNotNull(blobDiff3);
    }

    for (String branch : new String[] {branchA, branchB}) {
      DeleteBranchRequest deleteBranchRequest =
          DeleteBranchRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setBranch(branch)
              .build();
      versioningServiceBlockingStub.deleteBranch(deleteBranchRequest);
    }

    for (Commit commit : new Commit[] {commitB, commitA}) {
      DeleteCommitRequest deleteCommitRequest =
          DeleteCommitRequest.newBuilder()
              .setRepositoryId(
                  RepositoryIdentification.newBuilder().setRepoId(repository.getId()).build())
              .setCommitSha(commit.getCommitSha())
              .build();
      versioningServiceBlockingStub.deleteCommit(deleteCommitRequest);
    }

    LOGGER.info("Compute repository diff with one branch one commit test end....");
  }

  private void createBranch(Long repoId, String branch, String commitSHA) {
    SetBranchRequest setBranchRequest =
        SetBranchRequest.newBuilder()
            .setRepositoryId(RepositoryIdentification.newBuilder().setRepoId(repoId).build())
            .setBranch(branch)
            .setCommitSha(commitSHA)
            .build();
    versioningServiceBlockingStub.setBranch(setBranchRequest);
  }

  private Commit createCommit(String... parentCommits) {
    return Commit.newBuilder()
        .setMessage("this is the test commit message")
        .setDateCreated(Calendar.getInstance().getTimeInMillis())
        .addAllParentShas(Arrays.asList(parentCommits))
        .build();
  }

  private static List<String> LOCATION1 =
      Arrays.asList("modeldb", "march", "environment", FIRST_NAME);
  private static List<String> LOCATION2 = Arrays.asList("modeldb", "environment", SECOND_NAME);
  private static List<String> LOCATION3 = Arrays.asList("modeldb", "blob", "march", "blob.json");
  private static List<String> LOCATION4 = Collections.singletonList("modeldb.json");
  private static List<String> LOCATION5 = Collections.singletonList("maths/algebra");

  private BlobDiff deleteBlobDiff1(int blobType) {
    switch (blobType) {
      case 1:
        Builder test =
            HyperparameterConfigDiff.newBuilder()
                .setStatus(DiffStatus.DELETED)
                .setA(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test")
                        .setValue(
                            HyperparameterValuesConfigBlob.newBuilder().setIntValue(7).build())
                        .build());
        BlobDiff blobDiff1 =
            BlobDiff.newBuilder()
                .setStatus(DiffStatus.DELETED)
                .setConfig(ConfigDiff.newBuilder().addHyperparameters(test))
                .addAllLocation(LOCATION1)
                .build();
        return blobDiff1;
      default:
        CodeDiff.Builder builderForValue =
            CodeDiff.newBuilder()
                .setGit(
                    GitCodeDiff.newBuilder()
                        .setStatus(DiffStatus.DELETED)
                        .setA(
                            GitCodeBlob.newBuilder()
                                .setBranch("master")
                                .setRepo("git://github.com/VertaAI")
                                .build()));
        return BlobDiff.newBuilder()
            .setCode(builderForValue)
            .setStatus(DiffStatus.DELETED)
            .addAllLocation(LOCATION1)
            .build();
    }
  }

  private BlobDiff deleteBlobDiff4(int blobType) {
    switch (blobType) {
      case 1:
        return BlobDiff.newBuilder()
            .setStatus(DiffStatus.DELETED)
            .setConfig(
                ConfigDiff.newBuilder()
                    .addHyperparameterSet(
                        HyperparameterSetConfigDiff.newBuilder()
                            .setStatus(DiffStatus.DELETED)
                            .setA(
                                HyperparameterSetConfigBlob.newBuilder()
                                    .setName("name")
                                    .setContinuous(
                                        ContinuousHyperparameterSetConfigBlob.newBuilder()
                                            .setIntervalBegin(
                                                HyperparameterValuesConfigBlob.newBuilder()
                                                    .setFloatValue(5))
                                            .setIntervalEnd(
                                                HyperparameterValuesConfigBlob.newBuilder()
                                                    .setFloatValue(6))
                                            .setIntervalStep(
                                                HyperparameterValuesConfigBlob.newBuilder()
                                                    .setFloatValue(1))))))
            .addAllLocation(LOCATION4)
            .build();
      default:
        CodeDiff.Builder builderForValue =
            CodeDiff.newBuilder()
                .setGit(
                    GitCodeDiff.newBuilder()
                        .setStatus(DiffStatus.DELETED)
                        .setA(
                            GitCodeBlob.newBuilder()
                                .setBranch("master")
                                .setRepo("git://github.com/VertaAI")
                                .build()));
        return BlobDiff.newBuilder()
            .setCode(builderForValue)
            .setStatus(DiffStatus.DELETED)
            .addAllLocation(LOCATION4)
            .build();
    }
  }

  private BlobExpanded modifiedBlobExpanded(int blobType) {
    String path3 = "/protos/proto/public/test22.txt";
    BlobExpanded blobExpanded3 =
        BlobExpanded.newBuilder()
            .setBlob(getDatasetBlobFromPath(path3))
            .addAllLocation(LOCATION3)
            .build();

    return blobExpanded3;
  }

  private BlobDiff modifiedBlobDiff(int blobType) {
    switch (blobType) {
      case 1:
        Builder test =
            HyperparameterConfigDiff.newBuilder()
                .setStatus(DiffStatus.MODIFIED)
                .setA(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test2")
                        .setValue(HyperparameterValuesConfigBlob.newBuilder().setIntValue(7)))
                .setB(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test2")
                        .setValue(
                            HyperparameterValuesConfigBlob.newBuilder().setIntValue(5).build())
                        .build());
        return BlobDiff.newBuilder()
            .addAllLocation(LOCATION3)
            .setStatus(DiffStatus.MODIFIED)
            .setConfig(ConfigDiff.newBuilder().addHyperparameters(test))
            .build();
      default:
        CodeDiff.Builder builderForValue =
            CodeDiff.newBuilder()
                .setNotebook(
                    NotebookCodeDiff.newBuilder()
                        .setGitRepo(
                            GitCodeDiff.newBuilder()
                                .setStatus(DiffStatus.ADDED)
                                .setB(
                                    GitCodeBlob.newBuilder()
                                        .setBranch("master")
                                        .setRepo("git://github.com/VertaAI")
                                        .build()))
                        .setPath(
                            PathDatasetComponentDiff.newBuilder()
                                .setStatus(DiffStatus.ADDED)
                                .setB(
                                    getDatasetBlobFromPath("test")
                                        .getDataset()
                                        .getPath()
                                        .getComponents(0))));
        BlobDiff blobDiff =
            BlobDiff.newBuilder()
                .setCode(builderForValue)
                .setStatus(DiffStatus.ADDED)
                .addAllLocation(LOCATION3)
                .build();
        return blobDiff;
    }
  }

  private BlobDiff[] createDiffs(int blobType) {
    final BlobDiff blobDiff1, blobDiff2, blobDiff3, blobDiff4, blobDiff5;
    switch (blobType) {
      case 1:
        Builder test =
            HyperparameterConfigDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setB(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test")
                        .setValue(
                            HyperparameterValuesConfigBlob.newBuilder().setIntValue(7).build())
                        .build());
        blobDiff1 =
            BlobDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setConfig(ConfigDiff.newBuilder().addHyperparameters(test))
                .addAllLocation(LOCATION1)
                .build();

        Builder test2 =
            HyperparameterConfigDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setB(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test2")
                        .setValue(
                            HyperparameterValuesConfigBlob.newBuilder().setIntValue(5).build())
                        .build());
        blobDiff2 =
            BlobDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setConfig(ConfigDiff.newBuilder().addHyperparameters(test2))
                .addAllLocation(LOCATION2)
                .build();

        Builder test3 =
            HyperparameterConfigDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setB(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test2")
                        .setValue(
                            HyperparameterValuesConfigBlob.newBuilder().setIntValue(7).build())
                        .build());
        blobDiff3 =
            BlobDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setConfig(ConfigDiff.newBuilder().addHyperparameters(test3))
                .addAllLocation(LOCATION3)
                .build();

        blobDiff4 =
            BlobDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setConfig(
                    ConfigDiff.newBuilder()
                        .addHyperparameterSet(
                            HyperparameterSetConfigDiff.newBuilder()
                                .setStatus(DiffStatus.ADDED)
                                .setB(
                                    HyperparameterSetConfigBlob.newBuilder()
                                        .setName("name")
                                        .setContinuous(
                                            ContinuousHyperparameterSetConfigBlob.newBuilder()
                                                .setIntervalBegin(
                                                    HyperparameterValuesConfigBlob.newBuilder()
                                                        .setFloatValue(5))
                                                .setIntervalEnd(
                                                    HyperparameterValuesConfigBlob.newBuilder()
                                                        .setFloatValue(6))
                                                .setIntervalStep(
                                                    HyperparameterValuesConfigBlob.newBuilder()
                                                        .setFloatValue(1))))))
                .addAllLocation(LOCATION4)
                .build();

        Builder test5 =
            HyperparameterConfigDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setB(
                    HyperparameterConfigBlob.newBuilder()
                        .setName("test")
                        .setValue(
                            HyperparameterValuesConfigBlob.newBuilder().setIntValue(7).build())
                        .build());
        blobDiff5 =
            BlobDiff.newBuilder()
                .setStatus(DiffStatus.ADDED)
                .setConfig(ConfigDiff.newBuilder().addHyperparameters(test5))
                .addAllLocation(LOCATION5)
                .build();
        break;
      default:
        CodeDiff.Builder builderForValue =
            CodeDiff.newBuilder()
                .setGit(
                    GitCodeDiff.newBuilder()
                        .setStatus(DiffStatus.ADDED)
                        .setB(
                            GitCodeBlob.newBuilder()
                                .setBranch("master")
                                .setRepo("git://github.com/VertaAI")
                                .build()));
        blobDiff1 =
            BlobDiff.newBuilder()
                .setCode(builderForValue)
                .setStatus(DiffStatus.ADDED)
                .addAllLocation(LOCATION1)
                .build();
        blobDiff2 =
            BlobDiff.newBuilder()
                .setCode(builderForValue)
                .setStatus(DiffStatus.ADDED)
                .addAllLocation(LOCATION2)
                .build();
        blobDiff3 =
            BlobDiff.newBuilder()
                .setCode(builderForValue)
                .setStatus(DiffStatus.ADDED)
                .addAllLocation(LOCATION3)
                .build();
        blobDiff4 =
            BlobDiff.newBuilder()
                .setCode(builderForValue)
                .setStatus(DiffStatus.ADDED)
                .addAllLocation(LOCATION4)
                .build();
        blobDiff5 =
            BlobDiff.newBuilder()
                .setCode(builderForValue)
                .setStatus(DiffStatus.ADDED)
                .addAllLocation(LOCATION5)
                .build();
    }

    return new BlobDiff[] {blobDiff1, blobDiff2, blobDiff3, blobDiff4, blobDiff5};
  }

  private BlobExpanded[] createBlobs(int blobType) {
    final BlobExpanded blobExpanded1, blobExpanded2, blobExpanded3, blobExpanded4, blobExpanded5;
    switch (blobType) {
      case 0:
        String path1 = "/protos/proto/public/versioning/versioning.proto";
        blobExpanded1 =
            BlobExpanded.newBuilder()
                .setBlob(getDatasetBlobFromPath(path1))
                .addAllLocation(LOCATION1)
                .build();

        blobExpanded2 =
            BlobExpanded.newBuilder()
                .setBlob(getDatasetBlobFromPath(path1))
                .addAllLocation(LOCATION2)
                .build();

        blobExpanded3 =
            BlobExpanded.newBuilder()
                .setBlob(getDatasetBlobFromPath(path1))
                .addAllLocation(LOCATION3)
                .build();

        String path4 = "xyz.txt";
        blobExpanded4 =
            BlobExpanded.newBuilder()
                .setBlob(getDatasetBlobFromPath(path4))
                .addAllLocation(LOCATION4)
                .build();

        String path5 = "/protos/proto/public/algebra.txt";
        blobExpanded5 =
            BlobExpanded.newBuilder()
                .setBlob(getDatasetBlobFromPath(path5))
                .addAllLocation(LOCATION5)
                .build();
        break;
      default:
        PythonEnvironmentBlob.Builder pythonBuilder =
            PythonEnvironmentBlob.newBuilder()
                .addRequirements(
                    PythonRequirementEnvironmentBlob.newBuilder()
                        .setLibrary("numpy")
                        .setConstraint(">=")
                        .setVersion(
                            VersionEnvironmentBlob.newBuilder()
                                .setMajor(1)
                                .setMinor(18)
                                .setPatch(1)))
                .addRequirements(
                    PythonRequirementEnvironmentBlob.newBuilder()
                        .setLibrary("flask")
                        .setVersion(
                            VersionEnvironmentBlob.newBuilder()
                                .setMajor(1)
                                .setMinor(1)
                                .setPatch(1)));

        EnvironmentBlob.Builder builder =
            EnvironmentBlob.newBuilder()
                .addAllCommandLine(Arrays.asList("ECHO 123", "ls ..", "make all"))
                .addEnvironmentVariables(
                    EnvironmentVariablesBlob.newBuilder()
                        .setValue("/tmp/diff")
                        .setName("DIFF_LOCATION"));
        blobExpanded1 =
            BlobExpanded.newBuilder()
                .setBlob(Blob.newBuilder().setEnvironment(builder.setPython(pythonBuilder)))
                .addAllLocation(LOCATION1)
                .build();

        pythonBuilder.addConstraints(
            PythonRequirementEnvironmentBlob.newBuilder()
                .setLibrary("boto")
                .setConstraint("<=")
                .setVersion(
                    VersionEnvironmentBlob.newBuilder().setMajor(1).setMinor(1).setPatch(11)));
        Blob.Builder builderForBlob =
            Blob.newBuilder().setEnvironment(builder.setPython(pythonBuilder));
        blobExpanded2 =
            BlobExpanded.newBuilder().setBlob(builderForBlob).addAllLocation(LOCATION2).build();

        blobExpanded3 =
            BlobExpanded.newBuilder().setBlob(builderForBlob).addAllLocation(LOCATION3).build();

        blobExpanded4 =
            BlobExpanded.newBuilder().setBlob(builderForBlob).addAllLocation(LOCATION4).build();

        blobExpanded5 =
            BlobExpanded.newBuilder().setBlob(builderForBlob).addAllLocation(LOCATION5).build();
    }
    return new BlobExpanded[] {
      blobExpanded1, blobExpanded2, blobExpanded3, blobExpanded4, blobExpanded5
    };
  }
}
