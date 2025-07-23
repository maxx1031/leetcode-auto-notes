# 213. House Robber II

## 1. Clarifying Questions
Before diving into the solution, it's important to clarify the problem constraints and edge cases with the interviewer. Here are a few valuable questions:

- **Q: What is the maximum size of the input array (`nums`)?**  
  → *Typical Answer*: The size of the array can go up to 10^4, so the solution should be efficient in both time and space complexity.

- **Q: Can the input array contain negative numbers?**  
  → *Typical Answer*: No, the input array will only contain non-negative integers, as it represents the amount of money in each house.

- **Q: What should be returned if there is only one house?**  
  → *Typical Answer*: If there is only one house, the amount of money in that house should be returned as the result.

---

## 2. Algorithm & Data Structure
This problem falls under the category of **Dynamic Programming**. The goal is to maximize the amount of money robbed while adhering to the constraint that adjacent houses cannot both be robbed. Since the houses form a circular arrangement, we need to handle two separate cases to avoid robbing the first and last houses simultaneously.

### Core Algorithmic Approaches:
1. **Dynamic Programming (Iterative with Array)**: Use a dynamic programming table (`dp`) to store the maximum amount robbed up to each house, considering whether the current house is robbed or skipped.
2. **Dynamic Programming (Space-Optimized)**: Use two variables instead of a `dp` array to iteratively track the maximum amounts robbed, reducing space complexity to O(1).

### Data Structure:
- **Dynamic Programming Table**: Used to store intermediate results for subproblems.
- **Variables**: Used for space-optimized DP solutions.

---

## 3. High-Level Description

### Approach 1: Dynamic Programming (Iterative with Array)
- **Core Idea**: Treat the circular problem as two linear problems:
  1. Rob houses from index `0` to `n-2` (excluding the last house).
  2. Rob houses from index `1` to `n-1` (excluding the first house).
- Use a `dp` array where `dp[i]` represents the maximum amount robbed up to house `i`.
- Transition formula:  
  `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`  
  Either skip the current house or rob it and add its value to the maximum from two houses ago.

### Approach 2: Dynamic Programming (Space-Optimized)
- **Core Idea**: Similar to Approach 1 but instead of using a `dp` array, maintain two variables:
  - `prev1`: Maximum robbed up to the previous house.
  - `prev2`: Maximum robbed up to two houses ago.
- Transition formula:  
  `current = max(prev1, prev2 + nums[i])`  
  Update `prev2` to `prev1`, and `prev1` to `current`.

---

## 4. Code (with Key Explanations)

### My Code: Dynamic Programming (Iterative with Array)
```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solve the House Robber II problem using dynamic programming.
        Handles the circular arrangement of houses by splitting into two linear cases.
        """
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            # Initialize the dp array
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            # Fill the dp array based on the transition formula
            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            
            return dp[-1]
        
        # Case 1: Rob from house 0 to n-2
        # Case 2: Rob from house 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

### Approach 2: Dynamic Programming (Space-Optimized)
```python
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Solve the House Robber II problem using space-optimized dynamic programming.
        Handles the circular arrangement of houses by splitting into two linear cases.
        """
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for num in houses:
                # Calculate the current maximum
                current = max(prev1, prev2 + num)
                # Update prev2 and prev1 for the next iteration
                prev2, prev1 = prev1, current
            return prev1

        # Case 1: Rob from house 0 to n-2
        # Case 2: Rob from house 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
```

---

## 5. Test Cases

| Case Description         | Input               | Output | Explanation                                                                 |
|---------------------------|---------------------|--------|-----------------------------------------------------------------------------|
| Single house              | `[5]`              | `5`    | Only one house, so return its value.                                        |
| Two houses                | `[2, 3]`           | `3`    | Rob the second house for maximum profit.                                   |
| Circular arrangement      | `[2, 3, 2]`        | `3`    | Rob either the first or the second house.                                   |
| Larger circular array     | `[1, 2, 3, 1]`     | `4`    | Rob the second and fourth houses.                                          |
| All houses with same value| `[10, 10, 10, 10]` | `20`   | Rob two non-adjacent houses for maximum profit.                             |

---

## 6. Complexity

| Approach                      | Time Complexity | Space Complexity |
|-------------------------------|-----------------|------------------|
| DP (Iterative with Array)     | O(n)            | O(n)             |
| DP (Space-Optimized)          | O(n)            | O(1)             |

### Justification:
- **Time Complexity**: Both approaches iterate through the list of houses twice (once for each case), resulting in O(n) time complexity.
- **Space Complexity**: The first approach uses a `dp` array of size O(n), while the second approach uses only two variables, achieving O(1) space complexity.

---

## 7. Follow-Up & Optimizations
1. **Streaming Data**: How would you handle the problem if the input array is provided as a stream of data (e.g., houses are added dynamically)?
   - *Hint*: Use a sliding window approach with constant space to maintain the maximum values for the last two houses.

2. **Generalization**: What if the houses are arranged in a grid instead of a circular array? How would you adapt the algorithm?

3. **Parallelization**: Can the two linear cases (0 to n-2 and 1 to n-1) be solved in parallel to speed up the computation?