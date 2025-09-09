import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest

# 模板根目录（该文件所在目录）
TEMPLATE_ROOT = Path(__file__).resolve().parent.parent

# 最终生成的项目目录名
GEN_FOLDER = "cookiecutter_debug_project_slug"

# 调试用 cookiecutter 配置（直接内联，避免外部文件依赖）
DEBUG_CONFIG = {
    "project_name": "cookiecutter_debug_project",
    "project_slug": "cookiecutter_debug_project_slug",
    "package_name": "cookiecutterdebugpackage",
    "project_description": "DEBUG_CONFIG: Temporary project for template debugging",
    "author_name": "cookiecutter_debug_user",
    "author_email": "debug@cookiecutter.example.com",
    "version": "0.0.0",
}


def run(cmd, cwd=None):
    """简单封装的 subprocess.run，抛出失败即异常"""
    print(f"🚀 Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=True,
    )


@pytest.fixture(scope="module")
def generated_project():
    """
    用 fixture 保证：
    1. 整个测试 session 只生成/清理一次
    2. 无论断言是否通过，最终都会删除临时目录
    """
    tmp_dir = tempfile.mkdtemp(prefix="cookiecutter_test_")
    try:
        # 创建用户配置文件（使用内联配置）
        user_config = {"default_context": DEBUG_CONFIG}

        import json

        config_file = Path(tmp_dir) / "user_config.json"
        config_file.write_text(json.dumps(user_config))

        # 1. 生成项目
        run(
            [
                "cookiecutter",
                str(TEMPLATE_ROOT),
                "--no-input",
                "--config-file",
                str(config_file),
                "--output-dir",
                tmp_dir,
            ]
        )
        proj_path = Path(tmp_dir) / GEN_FOLDER
        assert proj_path.is_dir(), "Project generation failed"
        yield proj_path
    finally:
        # 清理
        print("🧹 Cleaning up generated project...")
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_package_dir_name(generated_project: Path):
    """验证包目录名是否正确"""
    assert (generated_project / "cookiecutterdebugpackage").is_dir()


def test_placeholder_replaced(generated_project: Path):
    """验证占位符被替换"""
    pyproject = generated_project / "pyproject.toml"
    readme = generated_project / "README.md"

    assert pyproject.exists()
    assert "cookiecutter_debug_user" in pyproject.read_text()

    assert readme.exists()
    assert "# cookiecutter_debug_project" in readme.read_text()


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
