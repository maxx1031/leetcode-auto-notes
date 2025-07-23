# 2466. Count Ways To Build Good Strings

---

## 1. Clarifying Questions

What boundary conditions or constraints should I confirm with an interviewer before coding? (Provide at least 3 valuable questions with typical answers).

- **Q: What are the constraints on `low`, `high`, `zero`, and `one`?**  
  → Typical Answer: `low` and `high` are integers with `0 <= low <= high <= 10^5`. `zero` and `one` are positive integers with `1 <= zero, one <= high`.

- **Q: Should we account for cases where `low` or `high` are extreme values (e.g., very large or very small)?**  
  → Typical Answer: Yes, ensure scalability for large values and handle edge cases like `low = 0` or `high = 0`.

- **Q: Is there a specific format or modular arithmetic required for the result?**  
  → Typical Answer: Yes, the result must be returned modulo `10^9 + 7` to prevent overflow.

---

## 2. Algorithm & Data Structure

### Main Algorithm Category:
Dynamic Programming (DP) and Recursion with Memoization.

### Approaches:
- **Approach 1**: Recursion with Memoization (DFS with caching).
- **Approach 2**: Bottom-Up Dynamic Programming (Tabulation).

### Data Structure:
- **Used in Approach 1**: Cache (Memoization using Python's `@cache` decorator).  
- **Used in Approach 2**: Array (`dp[]` to store intermediate results).

---

## 3. High-Level Description

### Approach 1: Recursion with Memoization  
- Core Idea: Use DFS to explore all possible ways to construct strings of valid lengths. Cache results for overlapping subproblems.  
- Execution Flow:
  1. Define a recursive function `dfs(i)` that computes the number of ways to construct strings of length `i`.
  2. Base cases: Return `1` for `i == 0` (valid string of length 0) and `0` for `i < 0` (invalid lengths).
  3. For each valid length `i`, recursively compute results for `i-zero` and `i-one`.
  4. Sum up results for all lengths in the range `[low, high]`.

### Approach 2: Bottom-Up Dynamic Programming  
- Core Idea: Use a DP array `dp[i]` where `dp[i]` stores the number of ways to construct strings of length `i`. Build solutions incrementally from smaller lengths to larger ones.  
- Execution Flow:
  1. Initialize `dp[0] = 1` (base case: one way to construct a string of length 0).
  2. For each length `i` from `1` to `high`, compute `dp[i]` based on `dp[i-zero]` and `dp[i-one]`.
  3. Sum up results for all lengths in the range `[low, high]`.

---

## 4. Code (with Key Explanations)

### My Code: Recursion with Memoization
```python
class Solution:
    def countGoodStrings(self, low, high, zero, one):
        """
        Approach 1: Recursion with Memoization
        - Use DFS to explore all valid string lengths.
        - Cache results to avoid redundant computations.
        """
        MOD = 1_000_000_007

        @cache
        def dfs(i):
            # Base cases
            if i < 0:  # Invalid length
                return 0
            if i == 0:  # Valid string of length 0
                return 1
            
            # Recursive case: explore adding `zero` and `one`
            return (dfs(i - zero) + dfs(i - one)) % MOD

        # Sum results for all lengths in range [low, high]
        return sum(dfs(i) for i in range(low, high + 1)) % MOD
```

### Alternative Code: Bottom-Up Dynamic Programming
```python
class Solution:
    def countGoodStrings(self, low, high, zero, one):
        """
        Approach 2: Bottom-Up Dynamic Programming
        - Build solutions incrementally using a DP array.
        - dp[i]: number of ways to construct strings of length i.
        """
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * high  # Initialize DP array

        # Compute dp values for all lengths up to `high`
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD  # Apply modulo to prevent overflow

        # Sum results for lengths in range [low, high]
        return sum(dp[i] for i in range(low, high + 1)) % MOD
```

---

## 5. Test Cases

| Case Description        | Input (`low, high, zero, one`) | Output | Explanation                                                                 |
|--------------------------|-------------------------------|--------|-----------------------------------------------------------------------------|
| Minimum values          | `low=0, high=0, zero=1, one=1` | `1`    | Only one way to construct a string of length 0.                            |
| Small range             | `low=1, high=2, zero=1, one=1` | `3`    | Strings of lengths 1 and 2 can be constructed using `zero` and `one`.      |
| Larger range            | `low=3, high=5, zero=2, one=1` | `6`    | Recursive combinations for lengths 3, 4, and 5.                            |
| Edge case: large values | `low=100, high=105, zero=2, one=3` | `...` | Valid combinations for large ranges.                                       |
| Invalid combinations    | `low=1, high=2, zero=3, one=4` | `0`    | No valid strings can be constructed due to constraints.                    |

---

## 6. Complexity

| Approach               | Time Complexity          | Space Complexity             |
|-------------------------|--------------------------|------------------------------|
| Recursion with Memoization | `O(high * 2)` (due to caching) | `O(high)` for recursion stack |
| Bottom-Up DP           | `O(high)`                | `O(high)` for DP array        |

---

## 7. Follow-Up & Optimizations

1. **Streaming Data**: How can this algorithm be adapted to handle streaming input where `low`, `high`, `zero`, and `one` values change dynamically?  
2. **Space Optimization**: Can the DP array be reduced to a rolling array to save space?  
3. **Parallelization**: How can the computation for large ranges be optimized using parallel processing techniques?  

---