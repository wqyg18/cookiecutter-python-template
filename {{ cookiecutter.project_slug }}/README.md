{{ cookiecutter.project_description }}
同步环境 uv sync
添加依赖 uv add some_package

使用loguru管理日志,存储在logs/目录下


运行py文件
所有命令均应在项目根目录下执行
1. 根目录下file.py
uv run python file.py
2. 子目录下file.py
uv run python -m file.to.file

如果需要使用pip,必须要
uv run python -m pip