# 64. Minimum Path Sum

---

## 1. Clarifying Questions

What boundary conditions or constraints should I confirm with an interviewer before coding? Below are three valuable questions to ask:

- **Q: What are the constraints on the grid dimensions (`m` and `n`)?**  
  → **Typical Answer:** `1 <= m, n <= 200`. The grid size is small enough to allow both dynamic programming and recursive approaches.

- **Q: Can the grid contain negative values?**  
  → **Typical Answer:** No, the grid only contains non-negative integers.

- **Q: Should we handle edge cases like empty grids or single-cell grids?**  
  → **Typical Answer:** Yes, ensure the solution works for edge cases such as a grid with `m = 1` or `n = 1`.

---

## 2. Algorithm & Data Structure

### Main Algorithm Category
Dynamic Programming (DP) is the primary algorithmic approach to solve this problem.

### Approaches
1. **Recursive with Memoization (Top-Down DP):** Use a recursive function with memoization to calculate the minimum path sum.  
2. **2D Dynamic Programming (Bottom-Up DP):** Build a 2D DP table iteratively to store the minimum path sum at each cell.  
3. **1D Dynamic Programming (Space Optimization):** Use a single array to store the minimum path sum for the current row, reducing space complexity.

### Data Structure
- **Grid:** The input is represented as a 2D list.  
- **DP Array/Table:** Used to store intermediate results for minimum path sums.  

---

## 3. High-Level Description

### Approach 1: Recursive with Memoization (Top-Down DP)
- **Key Idea:** Use recursion to explore all possible paths from the top-left to the bottom-right of the grid, and memoize intermediate results to avoid redundant calculations.  
- **Execution Flow:**  
    1. Define a recursive function `dfs(i, j)` that calculates the minimum path sum to cell `(i, j)`.  
    2. Base cases: If `i < 0` or `j < 0`, return infinity (`inf`). If `(i, j)` is the top-left cell, return its value.  
    3. Recursively calculate the minimum path sum by considering the cell above and the cell to the left.  
    4. Use memoization to store results for faster computation.  

---

### Approach 2: 2D Dynamic Programming (Bottom-Up DP)
- **Key Idea:** Use a 2D DP table to iteratively calculate the minimum path sum at each cell starting from the top-left.  
- **Execution Flow:**  
    1. Initialize a DP table `f` with dimensions `(m+1, n+1)` and set boundary values to infinity (`inf`).  
    2. Iterate through the grid and compute the minimum path sum for each cell using values from adjacent cells (`top` and `left`).  
    3. Return the value at the bottom-right cell of the DP table.  

---

### Approach 3: 1D Dynamic Programming (Space Optimization)
- **Key Idea:** Reduce space complexity by using a single array to store the minimum path sums for the current row.  
- **Execution Flow:**  
    1. Initialize a 1D array `f` with size `(n+1)` and set boundary values to infinity (`inf`).  
    2. Iterate through the grid row by row, updating the array values based on the minimum path sums from adjacent cells (`left` and `top`).  
    3. Return the last element of the array after processing all rows.  

---

## 4. Code (with Key Explanations)

### Approach 1: Recursive with Memoization (Top-Down DP)
```python
from functools import cache
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach 1: Recursive with Memoization
        - Use recursion to explore all paths and memoize results to avoid redundant calculations.
        """
        @cache
        def dfs(i: int, j: int) -> int:
            # Base cases
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[i][j]
            # Recursive step
            return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
        
        # Start recursion from bottom-right corner
        return dfs(len(grid) - 1, len(grid[0]) - 1)
```

---

### Approach 2: 2D Dynamic Programming (Bottom-Up DP)
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach 2: 2D Dynamic Programming
        - Build a DP table iteratively to store the minimum path sum at each cell.
        """
        m, n = len(grid), len(grid[0])
        # Initialize DP table
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 0  # Boundary condition
        
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        
        # Return the bottom-right value
        return dp[m][n]
```

---

### Approach 3: 1D Dynamic Programming (Space Optimization)
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Approach 3: 1D Dynamic Programming
        - Use a single array to reduce space complexity.
        """
        n = len(grid[0])
        dp = [float('inf')] * (n + 1)
        dp[1] = 0  # Boundary condition
        
        for row in grid:
            for j, value in enumerate(row):
                dp[j + 1] = min(dp[j], dp[j + 1]) + value
        
        # Return the last value in the array
        return dp[n]
```

---

## 5. Test Cases

| Case Description       | Input                            | Output | Explanation                                                                 |
|------------------------|----------------------------------|--------|-----------------------------------------------------------------------------|
| Normal Case            | `[[1,3,1],[1,5,1],[4,2,1]]`     | `7`    | Path: 1 → 3 → 1 → 1 → 1.                                                   |
| Single Row Grid        | `[[1,2,3]]`                     | `6`    | Only one possible path: 1 → 2 → 3.                                         |
| Single Column Grid     | `[[1],[2],[3]]`                 | `6`    | Only one possible path: 1 → 2 → 3.                                         |
| Large Values           | `[[100,200],[300,400]]`         | `1000` | Path: 100 → 200 → 400.                                                     |
| Edge Case (1x1 Grid)   | `[[5]]`                         | `5`    | Only one cell, so the minimum path sum equals the cell value.              |

---

## 6. Complexity

| Approach               | Time Complexity      | Space Complexity         |
|------------------------|----------------------|---------------------------|
| Recursive + Memoization| \(O(m \times n)\)   | \(O(m \times n)\), for memoization table. |
| 2D DP                  | \(O(m \times n)\)   | \(O(m \times n)\), for DP table.          |
| 1D DP (Space Optimized)| \(O(m \times n)\)   | \(O(n)\), for single-row DP array.        |

---

## 7. Follow-Up & Optimizations

1. **Streaming Data:** How would you handle streaming grid data where rows arrive one at a time?  
   → Use a sliding window approach to update the DP array for each row.

2. **Diagonal Movement:** What if diagonal movement is allowed in addition to right and down?  
   → Update the recurrence relation to include diagonal cells: `min(top, left, diagonal)`.

3. **Parallel Computation:** Can this problem be parallelized for larger grids?  
   → Divide the grid into subproblems and compute results for each sub-grid in parallel. Combine results at boundaries.