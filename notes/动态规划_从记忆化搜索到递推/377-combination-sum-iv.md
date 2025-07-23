```markdown
# 377. Combination Sum IV

---

## 1. Clarifying Questions
What boundary conditions or constraints should I confirm with an interviewer before coding? (Provide at least 3 valuable questions with typical answers).

Q: Can the input array `nums` contain negative numbers or zeros?  
→ No, `nums` will only contain positive integers as per the problem constraints.  

Q: Can the same number be used multiple times in a combination?  
→ Yes, you can reuse the same number multiple times to form a valid combination.  

Q: Does the order of numbers in a combination matter?  
→ Yes, the order of numbers matters, and different orders are considered distinct combinations (permutations).  

---

## 2. Algorithm & Data Structure
Briefly list the multiple core algorithmic approaches and required data structures to solve this problem.  

**Main Algorithm Category**: Dynamic Programming (DP), Depth-First Search (DFS) with Memoization  

- **Approach 1**: Recursive DFS with Memoization  
- **Approach 2**: Bottom-Up Dynamic Programming (Tabulation)  

**Data Structure**:  
- A 1D array (`dp`) for tabulation in the DP approach.  
- A hash table (or LRU cache) for memoization in the DFS approach.  

---

## 3. High-Level Description
Briefly describe the execution flow for each major approach.  

### Approach 1: Recursive DFS with Memoization  
- Use recursion to explore all possible combinations to reach the target.  
- For each recursive call, reduce the target by the current number from `nums`.  
- Use memoization (via an LRU cache) to store results of previously computed subproblems to avoid redundant computations.  

### Approach 2: Bottom-Up Dynamic Programming (Tabulation)  
- Use a 1D DP array where `dp[i]` represents the number of combinations to form the target `i`.  
- Start with `dp[0] = 1` (base case: there is one way to form target 0, which is using no numbers).  
- For each target from `1` to `target`, iterate through `nums` and update `dp[i]` by adding `dp[i - num]` for all valid `num` values.  

---

## 4. Code (with Key Explanations)

### My Code: Bottom-Up Dynamic Programming
```python
"""
Approach 2: Bottom-Up Dynamic Programming (Tabulation)
- Use a DP array where dp[i] represents the number of ways to form the target i.
- Iterate through each possible target from 1 to the given target.
- For each target, iterate through nums and update dp[i] by adding dp[i - num].
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize the DP array with dp[0] = 1 (base case)
        dp = [1] + [0] * target
        
        # Fill the DP array for all targets from 1 to target
        for i in range(1, target + 1):
            # Sum up all valid combinations for the current target i
            dp[i] = sum(dp[i - num] for num in nums if num <= i)
        
        # Return the result for the given target
        return dp[-1]
```

### Approach 1: Recursive DFS with Memoization
```python
"""
Approach 1: Recursive DFS with Memoization
- Use recursion to explore all possible combinations to reach the target.
- Use memoization to store results of previously computed subproblems.
"""
from functools import lru_cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(remaining):
            # Base case: If remaining target is 0, there's 1 valid combination
            if remaining == 0:
                return 1
            # Base case: If remaining target is negative, no valid combination
            if remaining < 0:
                return 0
            
            # Recursive case: Sum up combinations by reducing the target
            return sum(dfs(remaining - num) for num in nums)
        
        # Start the DFS with the full target
        return dfs(target)
```

---

## 5. Test Cases
Use a Markdown table to provide at least 5 representative test cases, covering normal, edge, and special scenarios.

| Case Description         | Input (`nums`, `target`) | Output | Explanation                                                                 |
|---------------------------|--------------------------|--------|-----------------------------------------------------------------------------|
| Normal case               | `[1, 2, 3], 4`          | `7`    | There are 7 permutations: `[1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2], ...`|
| Single element, valid     | `[1], 4`                | `1`    | Only one way: `[1,1,1,1]`.                                                  |
| Single element, invalid   | `[2], 3`                | `0`    | No way to form target 3 with only `2`.                                      |
| Empty `nums`              | `[], 5`                 | `0`    | No numbers available to form the target.                                    |
| Large target, small nums  | `[1, 2], 10`            | `89`   | Many permutations using numbers `1` and `2`.                                |

---

## 6. Complexity
Use a Markdown table to analyze the time and space complexity for each major approach, including a brief justification.

| Approach                     | Time Complexity | Space Complexity | Justification                                                                 |
|------------------------------|-----------------|------------------|-------------------------------------------------------------------------------|
| Recursive DFS with Memoization | O(T * N)       | O(T)            | T = target, N = len(nums). Each subproblem is solved once and cached.        |
| Bottom-Up Dynamic Programming | O(T * N)       | O(T)            | T = target, N = len(nums). Iteration over targets and nums fills the DP array.|

---

## 7. Follow-Up & Optimizations
Propose 2-3 insightful follow-up questions or optimization directions.

1. **Follow-Up**: What if `nums` contains duplicate values?  
   → Deduplicate `nums` before processing, as duplicates do not affect the result.  

2. **Follow-Up**: How can we handle very large targets efficiently?  
   → Use modular arithmetic to keep values manageable or optimize the DP approach further.  

3. **Follow-Up**: How would the solution change if the order of numbers in a combination does not matter?  
   → Use a combination-based approach (e.g., coin change problem) instead of permutations.  
```