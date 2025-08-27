# {{ cookiecutter.project_name }}

> {{ cookiecutter.project_description }}

<!-- 在这里添加你的项目徽章, 例如: CI/CD, Code Coverage, etc. -->
<!--
[![Build Status](...)]()
[![Coverage Status](...)]()
-->

---

## 目录

- [🚀 快速开始](#-快速开始)
- [⚙️ 开发指南](#️-开发指南)
  - [环境与依赖管理](#环境与依赖管理)
  - [运行代码](#运行代码)
  - [日志系统](#日志系统)
  - [代码测试](#代码测试)
  - [使用 Makefile](#使用-makefile)
- [📁 项目结构](#-项目结构)
- [🤝 贡献指南](#-贡献指南)
- [📄 许可证](#-许可证)

## 🚀 快速开始

1. **克隆仓库**
   ```bash
   git clone <your-repository-url>
   cd {{ cookiecutter.project_slug }}
   ```

2. **同步开发环境**
   本项目使用 [uv](https://github.com/astral-sh/uv) 管理环境和依赖。执行以下命令创建虚拟环境并安装所有依赖：
   ```bash
   uv sync
   ```
   此命令会读取 `pyproject.toml` 和 `uv.lock` 文件，确保你拥有与项目完全一致的开发环境。

## ⚙️ 开发指南

所有命令都应在激活虚拟环境（通过`uv sync`自动创建）或使用 `uv run` 的项目根目录下执行。

### 环境与依赖管理

- **同步环境**:
  ```bash
  # 安装/更新至 lock 文件中指定的依赖版本
  uv sync
  ```

- **添加新的生产依赖**:
  ```bash
  # uv 会自动将其添加到 pyproject.toml 并更新 uv.lock
  uv add requests
  ```

- **添加新的开发依赖** (如 `black`, `ruff`):
  ```bash
  uv add --dev black
  ```

### 运行代码

使用 `uv run` 可以在项目的虚拟环境中执行命令，无需手动激活。

- **运行根目录下的Python脚本**:
  ```bash
  uv run python main.py  # 假设你有 main.py
  ```

- **运行包内的模块**:
  ```bash
  uv run python -m {{ cookiecutter.package_name }}.module  # 替换 module
  ```

### 日志系统

项目已集成 `Loguru`，可以直接在代码中使用。日志配置位于 `utils/logging.py`。

- **使用方法**:
  ```python
  from utils.logging import logger

  logger.info("这是一条普通的信息日志。")
  logger.warning("注意，这里有一个潜在问题。")
  logger.error("发生了一个错误！")
  ```
- **日志文件**: 日志会自动轮转并保存在项目根目录的 `logs/` 文件夹下。

### 代码测试

项目使用 `Pytest` 进行测试。

- **运行所有测试**:
  ```bash
  uv run pytest
  ```

- **运行指定文件的测试**:
  ```bash
  uv run pytest tests/test_example.py
  ```

- **查看测试覆盖率**:
  ```bash
  uv run pytest --cov={{ cookiecutter.package_name }}
  ```

### 使用 Makefile

为了简化常用操作，项目提供了一个 `Makefile`。

- **安装/同步环境**:
  ```bash
  make install
  ```

- **运行测试**:
  ```bash
  make test
  ```

- **代码格式化与检查** (假设你已添加 `black` 和 `ruff`):
  ```bash
  # 格式化代码
  make format

  # 检查代码规范
  make lint
  ```

## 📁 项目结构

```
.
├── {{ cookiecutter.package_name }}/     # 核心Python包
├── tests/               # 测试代码
├── utils/               # 通用工具
├── scripts/             # 独立脚本
├── examples/            # 示例
├── .gitignore
├── .python-version
├── Makefile
├── pyproject.toml       # 项目配置与依赖
├── README.md            # 本文档
└── uv.lock              # 依赖锁定
```

## 🤝 贡献指南

欢迎为本项目贡献代码！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交你的修改 (`git commit -m 'feat: Add some amazing feature'`)
4. 推送到你的分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 📄 许可证

本项目基于 MIT 许可证开源。详情请参阅 [LICENSE](LICENSE) 文件。