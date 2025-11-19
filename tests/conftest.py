import pytest
import tempfile
import shutil
import subprocess
from pathlib import Path

# 模板根目录（该文件所在目录的上一级）
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
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )

@pytest.fixture(scope="session")
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
        config_file.write_text(json.dumps(user_config), encoding="utf-8")

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
        try:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        except Exception as e:
            print(f"Warning: Failed to clean up {tmp_dir}: {e}")
