import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest




def test_package_dir_name(generated_project: Path):
    """验证包目录名是否正确"""
    assert (generated_project / "cookiecutterdebugpackage").is_dir()


def test_placeholder_replaced(generated_project: Path):
    """验证占位符被替换"""
    pyproject = generated_project / "pyproject.toml"
    readme = generated_project / "README.md"

    assert pyproject.exists()
    assert "cookiecutter_debug_user" in pyproject.read_text(encoding="utf-8")

    assert readme.exists()
    assert "# cookiecutter_debug_project" in readme.read_text(encoding="utf-8")


def test_generated_project_health(generated_project: Path):
    """验证生成的项目基本健康状态"""
    # 检查关键文件是否存在
    assert (generated_project / "pyproject.toml").exists()
    assert (generated_project / "README.md").exists()
    assert (generated_project / "main.py").exists()
    assert (generated_project / "cookiecutterdebugpackage" / "__init__.py").exists()

    # 检查包目录结构
    assert (generated_project / "utils").is_dir()
    assert (generated_project / "scripts").is_dir()
