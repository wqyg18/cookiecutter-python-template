format:
	uv run ruff check . --fix --select ALL
	uv run ruff format .
lint:
	uv run ruff check .
	uv run ruff format --check .
install:
	uv sync
test:
	uv run pytest