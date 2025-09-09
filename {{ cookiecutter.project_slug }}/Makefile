format:
	# 修复import排序
	uv run ruff check --select I --fix .
	# 格式化
	uv run ruff format .
lint:
	uv run ruff check --fix .
install:
	uv sync && git init && cp .vscode/settings.json.example .vscode/settings.json
test:
	uv run pytest -v tests/