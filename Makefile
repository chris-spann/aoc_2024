
.PHONY: generate_day run_day update_progress

test:
	@poetry run pytest

lint:
	@poetry run ruff check . --fix

format:
	@poetry run ruff format .

generate_day:
	@poetry run python utils/generate_day.py

run_day:
	@poetry run python -m solutions.day_$(day)

update_progress:
	@poetry run python utils/update_progress.py
