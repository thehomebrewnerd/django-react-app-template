SRC_DIR := .

.PHONY: lint
lint:
	flake8 $(SRC_DIR) && isort --check-only --recursive $(SRC_DIR)

.PHONY: lint-fix
lint-fix:
	isort --recursive $(SRC_DIR)