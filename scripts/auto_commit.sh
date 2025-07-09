#!/bin/bash

# 确保在任何命令失败时退出
set -e

# --- 1. 定义 Commit 类型 (遵循 Conventional Commits) ---
# 这些是预设的选项，你可以根据自己的习惯修改
types=(
  "feat:     ✨ A new feature"
  "fix:      🐛 A bug fix"
  "docs:     📝 Documentation only changes (e.g., updating README, adding notes)"
  "style:    💄 Changes that do not affect the meaning of the code (white-space, formatting, etc)"
  "refactor: ♻️ A code change that neither fixes a bug nor adds a feature"
  "perf:     ⚡️ A code change that improves performance"
  "test:     ✅ Adding missing tests or correcting existing tests"
  "chore:    🔨 Other changes that don't modify src or test files (e.g., build process, dependency updates)"
)

# --- 2. 交互式选择 Commit 类型 ---
echo "🤔 What type of change are you committing?"
PS3="👉 Please enter your choice (number): " # 设置 select 提示符
select opt in "${types[@]}"; do
  # 从用户选择的字符串中提取类型标签 (例如从 "feat: ..." 中提取 "feat")
  COMMIT_TYPE=$(echo "$opt" | awk -F: '{print $1}')
  
  # 如果用户输入了有效数字，则跳出循环
  if [[ -n "$COMMIT_TYPE" ]]; then
    break
  else
    echo "🚨 Invalid option. Please try again."
  fi
done

# --- 3. 交互式输入 Commit 描述 ---
echo -e "\n💬 Please enter a short, descriptive commit message (e.g., 'add solution for problem 107'):"
read -r COMMIT_SUBJECT

# 如果用户没有输入任何内容，给一个默认值
if [[ -z "$COMMIT_SUBJECT" ]]; then
  COMMIT_SUBJECT="update project files"
fi

# --- 4. 组合最终的 Commit Message ---
COMMIT_MSG="${COMMIT_TYPE}: ${COMMIT_SUBJECT}"

echo -e "\n----------------------------------------"
echo "✅ Git Commit Message Generated:"
echo "   $COMMIT_MSG"
echo "----------------------------------------"
read -p "Looks good? Press Enter to continue, or Ctrl+C to abort." -r

# --- 5. 执行 Git 命令 ---
echo -e "\n🚀 Staging all changes..."
git add .

# 检查是否有文件被暂存
if git diff --staged --quiet; then
  echo "✅ No changes to commit. Working tree is clean."
  exit 0
fi

echo "📝 Committing changes..."
git commit -m "$COMMIT_MSG"

echo "☁️ Pushing changes to remote repository..."
git push

echo -e "\n🎉 Done! Your progress has been successfully pushed to GitHub."