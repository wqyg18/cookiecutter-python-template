#!/usr/bin/env bash
set -e

file="$1"

# 工作区根目录（VSCode 执行 Code Runner 时的 cwd 一般就是工作区根目录）
workspace="$(pwd)"

# 去掉前缀 + .py 后缀
relpath="${file#$workspace/}"
module="${relpath%.py}"

# 把路径分隔符 / 换成 .
module="${module//\//.}"

cmd="uv run python -m $module"

echo "[Running] $cmd"
exec $cmd
