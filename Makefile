.PHONY: reset

spec:
	@echo === Generating the spec ===
	@./scripts/generate_spec.sh

sdk:
	@echo === Generating the SDK ===
	@./scripts/generate_sdk.sh

test:
	@echo === Testing the SDK ===
	@PYTHONPATH=python -m pytest test

lint:
	@echo === Linting the SDK ===
	@python -m pyright foundry

reset:
	@echo === Resetting the git state ===
	git checkout HEAD -- .
