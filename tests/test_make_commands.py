import os
import subprocess
import platform
from pathlib import Path

IS_WINDOWS = platform.system() == "Windows"

# 导入共享的fixture

def run(cmd, cwd=None):
    """简单封装的 subprocess.run，抛出失败即异常"""
    print(f"🚀 Running: {' '.join(cmd) if isinstance(cmd, list) else cmd}")
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=True,
        text=True,
        encoding="utf-8",
        capture_output=True,
    )


def test_make_format(generated_project: Path):
    """验证make format命令正常工作"""
    # 切换到生成的项目目录
    original_cwd = os.getcwd()
    try:
        os.chdir(generated_project)

        # 执行make format命令
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", "manage.ps1", "format"] if IS_WINDOWS else ["make", "format"]
        result = run(cmd)

        # 验证命令执行成功
        assert result.returncode == 0

    finally:
        os.chdir(original_cwd)


def test_make_lint(generated_project: Path):
    """验证make lint命令正常工作"""
    # 切换到生成的项目目录
    original_cwd = os.getcwd()
    try:
        os.chdir(generated_project)

        # 执行make lint命令
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", "manage.ps1", "lint"] if IS_WINDOWS else ["make", "lint"]
        result = run(cmd)

        # 验证命令执行成功
        assert result.returncode == 0

    finally:
        os.chdir(original_cwd)


def test_make_install(generated_project: Path):
    """验证make install命令正常工作，并确保自定义包被正确安装"""
    # 切换到生成的项目目录
    original_cwd = os.getcwd()
    try:
        os.chdir(generated_project)

        # 执行make install命令
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", "manage.ps1", "install"] if IS_WINDOWS else ["make", "install"]
        result = run(cmd)

        # 验证命令执行成功
        assert result.returncode == 0

        # 验证输出中包含自定义包的安装信息
        output = result.stdout + result.stderr
        # 检查包是否被正确安装（处理不同的输出格式）
        # 有时uv sync会显示详细的安装信息，有时只会审计
        assert "cookiecutterdebugpackage" in output or "Audited" in output

        # 验证虚拟环境目录存在
        assert (generated_project / ".venv").is_dir()

    finally:
        os.chdir(original_cwd)


def test_make_test(generated_project: Path):
    """验证make test命令正常工作"""
    # 切换到生成的项目目录
    original_cwd = os.getcwd()
    try:
        os.chdir(generated_project)

        # 执行make test命令
        cmd = ["powershell", "-ExecutionPolicy", "Bypass", "-File", "manage.ps1", "test"] if IS_WINDOWS else ["make", "test"]
        result = run(cmd)

        # 验证命令执行成功
        assert result.returncode == 0

    finally:
        os.chdir(original_cwd)
