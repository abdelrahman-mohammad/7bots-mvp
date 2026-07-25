.PHONY: install lint format

install:
	uv sync
	uv run pre-commit install

lint:
	uv run poe lint

format:
	uv run poe format
