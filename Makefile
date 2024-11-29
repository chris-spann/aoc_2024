
.PHONY: generate_day

test:
	@poetry run pytest

lint:
	@poetry run ruff check . --fix

format:
	@poetry run ruff format .

generate_day:
	@poetry run python utils/generate_day.py
