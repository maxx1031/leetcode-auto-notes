#!/bin/bash

# 确保脚本在任何命令失败时退出
set -e

echo "🚀 Starting automated commit process..."

# 1. 添加所有更改到暂存区
# 包括新生成的笔记、新写的 solution，以及可能更新的 todo.yml
git add .

# 2. 检查是否有文件被暂存
if git diff --staged --quiet; then
  echo "✅ No changes to commit. Working tree is clean."
  exit 0
fi

# 3. 创建一个有意义的提交信息
# 例如: "docs: Auto-generate LeetCode notes for 2023-10-27"
COMMIT_MSG="docs: Auto-generate LeetCode notes for $(date +'%Y-%m-%d')"

echo "📝 Committing changes with message: \"$COMMIT_MSG\""
git commit -m "$COMMIT_MSG"

# 4. 推送到远程仓库
echo "☁️ Pushing changes to remote repository..."
git push

echo "🎉 Done! Your LeetCode progress has been saved to GitHub."