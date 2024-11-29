test:
	@poetry run pytest

lint:
	@poetry run ruff check . --fix

format:
	@poetry run ruff format --check .
