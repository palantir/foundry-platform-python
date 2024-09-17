set -eu

# List of specific file paths to exclude
EXCLUDED_PATHS=(
    "Makefile"
    "scripts/generate_sdk.sh"
    "scripts/generate_spec.sh"
    "config.json"
    ".policy.yml"
    "changelog"
    ".git"
    "tmp"
    # Docs examples live here. These will go away eventually.
    "assets"
    # Unit tets are written manually
    "test"
    "venv"
)

TMP_DIR=$(mktemp -d)

for EXCLUDED_PATH in "${EXCLUDED_PATHS[@]}"; do
    TARGET_PATH="$TMP_DIR/$EXCLUDED_PATH"
    mkdir -p $(dirname $TARGET_PATH)
    cp -r $EXCLUDED_PATH $TARGET_PATH
done

# Remove everything in the current directory
shopt -s dotglob  # make sure to remove files that start with "."
rm -rf ./*

# Move files back from the temporary directory
rsync -av "$TMP_DIR/" ./ &> /dev/null

# Clean up the temporary directory
rm -rf "$TMP_DIR"

python -m platform_sdk_generator \
    --config_path config.json \
    --output_dir . \
    --manifest_path "tmp/manifest.yml" \
    --version v1 --ir_path "tmp/openapi-ir.json" \
    --version v2 --ir_path "tmp/openapi-ir.json" \
    --version v2 --ir_path "tmp/v2.json"
