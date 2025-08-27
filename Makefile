format:
	# 修复import排序
	uv run ruff check --select I --fix .
	# 格式化
	uv run ruff format .
lint:
	uv run ruff check .
install:
	uv sync
test:
	uv run pytest -v tests/