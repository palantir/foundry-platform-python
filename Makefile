.PHONY: reset test

spec:
	@echo === Generating the spec ===
	@./scripts/generate_spec.sh

sdk:
	@echo === Generating the SDK ===
	@./scripts/generate_sdk.sh

test:
	@echo === Testing the SDK ===
	@python -m pytest tests

format:
	@echo
	@echo === Formatting the Generator ===
	@isort foundry_sdk tests --profile black --multi-line NOQA -sl --project foundry_sdk
	@python -m black foundry_sdk tests

lint:
	@echo === Linting the SDK ===
	@python -m pyright foundry_sdk

reset:
	@echo === Resetting the git state ===
	git checkout HEAD -- .
