.PHONY: install
install:
	pipx install poetry==1.7.1
	poetry install && poetry build

.PHONY: lint
lint:
	poetry run ruff check .
	poetry run ruff format --check .

.PHONY: format
format:
	poetry run ruff format .

# Lcov report included for vscode coverage
.PHONY: test
test:
	poetry run coverage run
	poetry run coverage report

.PHONY: coverage-lcov
coverage-lcov:
	poetry run coverage lcov
