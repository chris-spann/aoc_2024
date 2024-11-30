.PHONY: test lint format typecheck generate_day run_day update_progress help

test:
	@poetry run pytest

lint:
	@poetry run ruff check . --fix

format:
	@poetry run ruff format .

typecheck:
	@poetry run pyright

generate_day:
	@poetry run python utils/generate_day.py

run_day:
	@if [ -z "$(day)" ]; then \
		echo "Error: Please provide the 'day' variable (e.g., make run_day day=1)"; \
		exit 1; \
	fi
	@poetry run python -m solutions.day_$(day)

update_progress:
	@poetry run python utils/update_progress.py

help:
	@echo "Usage: make <target>"
	@echo
	@echo "Available targets:"
	@echo "  test             Run tests using pytest"
	@echo "  lint             Lint code and apply autofixes using ruff"
	@echo "  format           Format code using ruff"
	@echo "  typecheck        Run type checking with pyright"
	@echo "  generate_day     Generate boilerplate for a new day's solution"
	@echo "  run_day          Run a specific day's solution (e.g., make run_day day=1)"
	@echo "  update_progress  Update progress in README based on commit messages"
	@echo "  help             Show this help message"
