# prompt_template.py
import re

def create_prompt(problem_data: dict, user_code: str) -> str:
    """Builds a high-quality prompt for GPT in English, designed for multi-solution analysis."""
    
    # Extract problem data
    problem_id = problem_data['questionFrontendId']
    title_slug = problem_data['titleSlug']
    title = problem_data.get('title', 'N/A') # Use the original English title
    
    difficulty = problem_data['difficulty']
    # Clean HTML tags from the description
    description_html =problem_data.get('content') or problem_data.get('translatedContent') or ''
    description_text = re.sub('<[^<]+?>', '', description_html).strip()
    
    # Construct the LeetCode link
    leetcode_link = f"https://leetcode.com/problems/{title_slug}/"
    
    approach1 = '"""\nApproach 1: [Approach Name]\n- [Core idea 1]\n- [Core idea 2]\n"""\n# Code for Approach 1...\n'
    approach2 = '"""\nApproach 2: [Approach Name]\n- [Core idea 1]\n- [Core idea 2]\n"""\n# Code for Approach 2...\n'

    # This is the new, ultimate prompt template in English
    prompt = f"""
You are a world-class algorithm expert and a LeetCode coach. Your task is to generate a professional, in-depth, and comparative study note in Markdown format based on the provided problem information and one of my solutions.

### Mission:
1.  **Identify My Solution**: Analyze my provided code to determine its core algorithmic approach (e.g., Pre-order Traversal, In-order Traversal, Dynamic Programming, Two Pointers, etc.).
2.  **Brainstorm Other Solutions**: In addition to my solution, conceptualize and describe 1-2 other common or optimal algorithms for this problem.
3.  **Strictly Format the Output**: You must strictly adhere to the format specified in the [Output Format] section below. Pay close attention to using Markdown tables for test cases and complexity analysis.

---

### [Problem Information]
**Title:** {title}
**Difficulty:** {difficulty}
**Description:**
{description_text}

---

### [My Code]
```python
{user_code}
```

[Output Format]
Please generate the response strictly using the following Markdown format, filling in all sections.
{problem_id}. {title}
1. Clarifying Questions
What boundary conditions or constraints should I confirm with an interviewer before coding? (Provide at least 3 valuable questions with typical answers).
Q: [Question 1]?
→ [Typical Answer].
Q: [Question 2]?
→ [Typical Answer].
Q: [Question 3]?
→ [Typical Answer].
2. Algorithm & Data Structure
Briefly list the multiple core algorithmic approaches and required data structures to solve this problem.
[Main Algorithm Category, e.g., Tree Traversal]:
[Approach 1 Name, e.g., Pre-order with range checking].
[Approach 2 Name, e.g., In-order with last visited value tracking].
[Approach 3 Name, e.g., Post-order with subtree min/max return].
Data Structure: [e.g., Binary Tree, Stack, HashMap]
3. High-Level Description
Briefly describe the execution flow for each major approach. Use "Approach X: [Approach Name]" as a title.
Approach 1: [Approach 1 Name]
...
...
Approach 2: [Approach 2 Name]
...
...
4. Code (with Key Explanations)
Feature [My Code] as one of the solutions, adding concise, insightful comments.
Additionally, provide clean, runnable Python code for the other major approaches described in Section 3, also with comments.
Start each code block with a docstring summary like ''' [Brief description of approach] '''.
"""
    prompt += approach1
    prompt += '\n'
    prompt += approach2
    prompt += """
5. Test Cases
Use a Markdown table to provide at least 5 representative test cases, covering normal, edge, and special scenarios.
Case    Input    Output    Explanation
[Case Description 1]    ...    True    [Brief reason]
[Case Description 2]    ...    False    [Brief reason]
...    ...    ...    ...
6. Complexity
Use a Markdown table to analyze the time and space complexity for each major approach, including a brief justification.
Approach    Time Complexity    Space Complexity
[Approach 1 Name]    O(...)    O(...), for recursion stack
[Approach 2 Name]    O(...)    O(...), for extra space
...    ...    ...
7. Follow-Up & Optimizations
Propose 2-3 insightful follow-up questions or optimization directions.
These can involve variations of the algorithm, its application in different scenarios, or extreme optimizations of time/space complexity.
Examples: How to handle streaming data? How to validate more complex structures (e.g., AVL/Red-Black Trees)? What if you need to design a BST iterator?
"""
    return prompt
