format:
	# 修复import排序
	uv run ruff check --select I --fix .
	# 格式化
	uv run ruff format .
lint:
	uv run ruff check --fix .
install:
	uv sync
test:
	uv run pytest -v tests/
debug:
	rm -rf /tmp/debug_project && cookiecutter . --no-input --output-dir /tmp/debug_project && cd /tmp/debug_project && echo "✅ Debug project created successfully!" && echo "📁 To enter the project directory, run: cd /tmp/debug_project/my_new_project"