
# 🚀 现代化 Python 项目模板

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![UV](https://img.shields.io/badge/package_manager-uv-orange)](https://github.com/astral-sh/uv)
[![Cookiecutter](https://img.shields.io/badge/template-cookiecutter-green)](https://cookiecutter.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/wqyg18/cookiecutter-python-template/graphs/commit-activity)

告别繁琐的项目初始化配置，专注于核心代码编写。本项目是一个基于 [Cookiecutter](https://cookiecutter.readthedocs.io/) 的现代化Python项目模板，集成了当前社区的最佳实践与高效的开发工具链，助你秒速开启新项目。

---

## ✨ 核心特性

- 🏗️ **标准化项目结构**: 遵循社区广泛认可的最佳实践，结构清晰，易于维护。
- ⚡ **一键式项目生成**: 通过 `cookiecutter` 命令行工具，交互式地完成项目初始化。
- 📦 **现代化包管理**: 内置 [**uv**](https://github.com/astral-sh/uv)，一个极速的Python包安装器和解析器，完全取代 `pip` 和 `venv`。
- 📝 **优雅的日志系统**: 集成 [**Loguru**](https://github.com/Delgan/loguru)，提供开箱即用、功能强大且对开发者友好的日志体验。
- 🧪 **完备的测试框架**: 预设 [**Pytest**](https://pytest.org/) 测试环境，让编写测试成为一种享受。
- 🛠️ **便捷的开发脚本**: 提供 `Makefile`，封装常用命令，如安装、测试、格式化等，简化开发流程。
- 📚 **清晰的文档指引**: 生成的项目自带一份详细的开发指南 `README.md`，新人也能快速上手。

## 🚀 如何使用

### 前置条件

确保你的开发环境中已安装以下工具：

- Python 3.8+
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)
- [uv](https://github.com/astral-sh/uv) (强烈推荐，用于后续项目开发)

### 生成你的项目

1. **安装 Cookiecutter** (如果尚未安装):
   ```bash
   pip install cookiecutter
   ```

2. **使用此模板创建新项目**:
   ```bash
   cookiecutter https://github.com/wqyg18/cookiecutter-python-template.git
   ```

3. **根据提示回答问题**:
   `cookiecutter` 会引导你输入项目名称、包名称、作者信息等，以定制化你的项目。

完成后，一个崭新的、配置完备的Python项目目录就创建好了！

## 📦 模板包含什么？

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.package_name }}/     # 你的核心Python包代码
│   └── __init__.py
├── tests/               # Pytest测试文件
├── utils/               # 通用工具模块
│   ├── __init__.py
│   └── logging.py       # Loguru 日志配置
├── scripts/             # 存放独立的脚本文件
├── examples/            # 示例代码目录
├── .gitignore           # Git忽略文件配置
├── .python-version      # 指定项目使用的Python版本 (pyenv会识别)
├── Makefile             # 自动化任务脚本 (如: make install, make test)
├── pyproject.toml       # 项目元数据与依赖管理 (PEP 621)
├── README.md            # ✨ 生成的项目自带的开发指南
└── uv.lock              # 依赖锁定文件，确保环境一致性
```

## 🎯 下一步：开始开发

项目生成后，请进入新创建的目录，并参考其中的 `README.md` 文件开始您的开发之旅。该文件包含了详细的环境设置、依赖管理、代码运行和测试指南。

```bash
cd <your-new-project-slug>
cat README.md
```

## 🤝 如何贡献

欢迎对本 **模板** 提出改进建议！如果你有任何想法，请随时提交 Issue 或 Pull Request。

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的修改 (`git commit -m 'Add some amazing feature'`)
4. 推送到你的分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 🙏 致谢

- [Cookiecutter](https://cookiecutter.readthedocs.io/)
- [uv](https://github.com/astral-sh/uv)
- [Loguru](https://github.com/Delgan/loguru)

---

<p align="center">
  ⭐ 如果这个模板对你有帮助，请给个 Star 支持一下！ ⭐
</p>

---