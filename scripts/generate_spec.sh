set -eu

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
TMP_DIR=$SCRIPT_DIR/../tmp
MAVEN_REPO_PATH="$MAVEN_DIST_RELEASE/$(echo "$MAVEN_CONJURE_GROUP_ID" | sed 's/\./\//g')/${MAVEN_CONJURE_ARTIFACT_ID}"

mkdir -p $TMP_DIR
API_GATEWAY_VERSION=$( wget -q -O - "${MAVEN_REPO_PATH}/maven-metadata.xml" | \
    yq -p xml -r '.metadata.versioning.release' )

echo Downloading $API_GATEWAY_VERSION...
mkdir -p "${TMP_DIR}"
wget -P "${TMP_DIR}"  "${MAVEN_REPO_PATH}/${API_GATEWAY_VERSION}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" &> /dev/null

tar -xf "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=4 "${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}/asset/palantir/ir-v2/openapi-ir.json"
tar -xf "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=4 "${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}/asset/palantir/ir-v2/v2.json"
tar -xf "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=4 "${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}/asset/palantir/new-content/api-definition.yml"
tar -xf "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=2 "${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}/deployment/manifest.yml"

echo Done!
