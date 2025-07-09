# main_script.py
import os
import argparse
import re
from dotenv import load_dotenv
from openai import OpenAI

from leetcode_fetcher import get_leetcode_problem
from prompt_template import create_prompt

# 加载环境变量
load_dotenv()

# 初始化 OpenAI 客户端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                base_url=os.getenv("OPENAI_BASE_URL"))

def slugify(text: str) -> str:
    """将任意字符串转换为适合做文件/文件夹名的格式"""
    # 移除非法字符
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    # 用下划线替换空格和多个连字符
    text = re.sub(r'[-\s]+', '_', text)
    return text

def generate_notes(code_file_path: str, category: str = None, pre_fetched_slug: str = None) -> str:
    """主函数，执行整个自动化流程。返回一个状态字符串。"""
    
    if pre_fetched_slug:
        title_slug = pre_fetched_slug
    else:
        # 保持了单独运行 main_script.py 的能力
        base_name = os.path.basename(code_file_path)
        slug_with_ext = os.path.splitext(base_name)[0]
        title_slug = re.sub(r'^\d+-', '', slug_with_ext)
    
    print(f"🚀 Found problem slug: '{title_slug}' from file name.")
    print(f"🗂️ Category: {category if category else 'Default'}")

    # 1. 获取题目信息
    print("   Step 1/4: Fetching problem data from LeetCode...")
    problem_data = get_leetcode_problem(title_slug)
    if not problem_data:
        return "FETCH_FAILED"

    # ... (检查目标文件是否存在的逻辑) ...
    # ... (创建目录的逻辑) ...
    output_dir = "notes"
    if category:
        # 1. 创建分类子目录
        category_slug = slugify(category)
        output_dir = os.path.join(output_dir, category_slug)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = f"{problem_data['questionFrontendId']}-{problem_data['titleSlug']}.md"
    file_path = os.path.join(output_dir, file_name)
    
    if os.path.exists(file_path):
        print(f"✅ SKIPPED: Note already exists at '{file_path}'.")
        return "SKIPPED"

    # ... (剩下的代码，从 "读取你的代码" 到 "保存为 Markdown 文件") ...
    # 2. 读取你的代码
    print("   Step 2/4: Reading your solution code...")
    try:
        with open(code_file_path, 'r', encoding='utf-8') as f:
            user_code = f.read()
    except FileNotFoundError:
        print(f"❌ ERROR: Code file not found at '{code_file_path}'")
        return

    # 3. 创建 Prompt
    print("   Step 3/4: Building intelligent prompt for GPT...")
    prompt = create_prompt(problem_data, user_code)

    # 4. 调用 OpenAI API
    print("   Step 4/4: Calling GPT to generate notes... (this may take a moment)")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output well-structured Markdown in English."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        generated_notes = response.choices[0].message.content
    except Exception as e:
        print(f"❌ ERROR: Failed to call OpenAI API: {e}")
        return

    # 5. 保存为 Markdown 文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(generated_notes)
    # 在成功保存后
    print(f"\n✅ SUCCESS! Note saved to: {file_path}")
    return "SUCCESS"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Auto-generate LeetCode study notes from your solution file.")
    
    # 位置参数：代码文件路径 (必需)
    parser.add_argument("code_file", type=str, help="Path to your solution code file (e.g., 'solutions/236-lca.py'). The script will infer the problem slug from this.")
    
    # 可选参数：分类
    parser.add_argument("--category", type=str, help="The study list category (e.g., '二叉树与递归-最近的共同祖先'). A sub-directory will be created for it.")
    
    args = parser.parse_args()
    
    generate_notes(args.code_file, args.category)