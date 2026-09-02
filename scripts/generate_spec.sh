set -eu

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
TMP_DIR=$SCRIPT_DIR/../tmp
MAVEN_GROUP_PATH=$(echo "$MAVEN_CONJURE_GROUP_ID" | sed 's/\./\//g')
MAVEN_REPO_PATH="$MAVEN_DIST_RELEASE/${MAVEN_GROUP_PATH}/${MAVEN_CONJURE_ARTIFACT_ID}"
FEDERATED_IR_ARTIFACT_ID=api-gateway-federated-ir
FEDERATED_IR_REPO_PATH="$MAVEN_DIST_RELEASE/${MAVEN_GROUP_PATH}/${FEDERATED_IR_ARTIFACT_ID}"

mkdir -p $TMP_DIR

if [ -z "${API_GATEWAY_VERSION:-}" ]; then
    API_GATEWAY_VERSION=$( wget -q -O - "${MAVEN_REPO_PATH}/maven-metadata.xml" | \
        python scripts/parse_version.py )
fi

echo Downloading $API_GATEWAY_VERSION...
mkdir -p "${TMP_DIR}"
wget -O "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" "${MAVEN_REPO_PATH}/${API_GATEWAY_VERSION}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" &> /dev/null
wget -O "${TMP_DIR}/federated-ir.json" "${FEDERATED_IR_REPO_PATH}/${API_GATEWAY_VERSION}/${FEDERATED_IR_ARTIFACT_ID}-${API_GATEWAY_VERSION}.omni.json" &> /dev/null

tar -xf "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=4 "${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}/asset/palantir/ir-v2/combined-ir.json"
tar -xf "${TMP_DIR}/${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}.sls.tgz" -C "${TMP_DIR}" --strip-components=2 "${MAVEN_CONJURE_ARTIFACT_ID}-${API_GATEWAY_VERSION}/deployment/manifest.yml"

echo Done!
