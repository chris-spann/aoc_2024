test:
	@poetry run pytest

format:
	@poetry run ruff format --check .

lint:
	@poetry run ruff check . --fix
