#!/usr/bin/env python3
import os
import yaml  # 需要安装: pip install pyyaml
import argparse
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.process_single import generate_notes, slugify
from src.lc_automator.fetcher import get_problem_map

def batch_process_solutions(category: str):
    """
    根据 todo.yml 文件，批量处理指定分类下的所有解决方案。
    """
    # 1. 加载 YAML 控制文件
    try:
        with open("todo.yml", 'r', encoding='utf-8') as f:
            todo_data = yaml.safe_load(f)
    except FileNotFoundError:
        print("❌ 错误: `todo.yml` 文件未找到。请先创建它。")
        return

    if category not in todo_data:
        print(f"❌ 错误: 在 `todo.yml` 中找不到分类 '{category}'。")
        print(f"可用分类: {list(todo_data.keys())}")
        return

    # 2. 获取题目 ID->Slug 映射
    problem_map_data = get_problem_map()
    if not problem_map_data:
        print("❌ 无法获取题目映射，已终止。")
        return
    id_to_slug_map = problem_map_data['id_to_slug']

    # 3. 循环处理指定分类下的题目
    problem_ids = todo_data[category]
    print(f"🚀 开始批量处理分类 '{category}' 下的 {len(problem_ids)} 个题目...")
    
    success_count = 0
    processed_count = 0
    for problem_id in problem_ids:
        problem_id_str = str(problem_id)
        
        # 检查 solution 文件是否存在
        code_file_path = os.path.join("solutions", f"{problem_id_str}.py")
        if not os.path.exists(code_file_path):
            # 如果文件不存在，静默跳过，表示你还没写
            continue
        
        processed_count += 1
        print(f"\n M处理题目: {problem_id_str}")

        # 从映射中查找 titleSlug
        title_slug = id_to_slug_map.get(problem_id_str)
        if not title_slug:
            print(f"  └─ ⚠️ 警告: 在 LeetCode 题库中找不到 ID 为 {problem_id_str} 的题目，已跳过。")
            continue

        # 4. 调用主脚本的核心函数来生成笔记
        # generate_notes 函数内部会处理“已存在则跳过”的逻辑
        # 我们需要在 generate_notes 函数中返回一个状态
        try:
            # 改造 generate_notes 让它返回一个值来判断是否真的生成了
            status = generate_notes(code_file_path, category, pre_fetched_slug=title_slug)
            if status == "SUCCESS":
                success_count += 1
        except Exception as e:
            print(f"  └─ ❌ 处理 {code_file_path} 时发生严重错误: {e}")

    print(f"\n🎉 批量处理完成！")
    print(f"  - 在分类 '{category}' 中，你已完成 {processed_count}/{len(problem_ids)} 道题。")
    print(f"  - 本次新生成笔记 {success_count} 篇。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="根据 todo.yml 批量生成 LeetCode 笔记。")
    parser.add_argument("category", type=str, help="要处理的题单分类 (必须与 todo.yml 中的 key 完全一致)。")
    args = parser.parse_args()
    
    batch_process_solutions(args.category)