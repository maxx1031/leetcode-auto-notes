# leetcode_fetcher.py
# 它只会在第一次运行时请求一次 LeetCode API，然后将结果保存在 a_problem_map.json 文件中。之后每次运行都会直接读取本地缓存
import requests
import json
import os

def get_problem_map():
    """获取所有 LeetCode 题目的 ID->Slug 和 Slug->ID 的映射关系。
       为了效率，结果会缓存到 a_problem_map.json 文件中。"""
    
    cache_file = "a_problem_map.json"
    
    # 如果缓存文件存在，直接从缓存加载
    if os.path.exists(cache_file):
        with open(cache_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    print("正在从 LeetCode 获取题目列表以构建映射... (仅首次运行或缓存删除后发生)")
    url = "https://leetcode.com/api/problems/all/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        id_to_slug = {}
        slug_to_id = {}
        
        for problem in data['stat_status_pairs']:
            # 只关心免费题
            if not problem['paid_only']:
                question_id = problem['stat']['frontend_question_id']
                question_slug = problem['stat']['question__title_slug']
                id_to_slug[str(question_id)] = question_slug
                slug_to_id[question_slug] = str(question_id)

        problem_map = {"id_to_slug": id_to_slug, "slug_to_id": slug_to_id}
        
        # 写入缓存
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(problem_map, f)
            
        print("题目映射构建完成并已缓存。")
        return problem_map

    except requests.exceptions.RequestException as e:
        print(f"获取题目列表时网络错误: {e}")
        return None
    
def get_leetcode_problem(title_slug: str) -> dict:
    """根据题目的 titleSlug 获取详细信息"""
    url = "https://leetcode.com/graphql/" # 国内版用 .cn，国际版用 .com
    payload = {
        "query": """
            query getQuestionDetail($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                translatedTitle
                translatedContent
                difficulty
                topicTags {
                  name
                  slug
                  translatedName
                }
              }
            }
        """,
        "variables": {"titleSlug": title_slug},
        "operationName": "getQuestionDetail"
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        data = response.json()['data']['question']
        if not data:
            print(f"错误：找不到题目 '{title_slug}'。请检查题目的 a-z, 0-9, - 格式的名称。")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"网络请求错误: {e}")
        return None