# 3Sum Closest

## 1. Clarifying Questions

What boundary conditions or constraints should I confirm with an interviewer before coding? (Provide at least 3 valuable questions with typical answers).

Q: **What is the expected input size? Are there any constraints on the number of elements in the list?**  
→ Typical Answer: The list can contain up to 10,000 elements. You should consider the constraints to ensure your solution is efficient.

Q: **Can the input list contain negative numbers, and are there any duplicates allowed?**  
→ Typical Answer: Yes, the list can contain negative numbers and duplicates.

Q: **What should be done if multiple sums are equally close to the target?**  
→ Typical Answer: If multiple sums are equally close, returning any of them is acceptable.

## 2. Algorithm & Data Structure

Briefly list the multiple core algorithmic approaches and required data structures to solve this problem.

- **Main Algorithm Category:** Two Pointers
  - **Approach 1 Name:** Two Pointers with Sorting
  - **Approach 2 Name:** Brute Force Enumeration
  - **Approach 3 Name:** Optimized Two Pointers with Early Stopping
- **Data Structure:** Array

## 3. High-Level Description

Briefly describe the execution flow for each major approach.

### Approach 1: Two Pointers with Sorting

1. Sort the array to facilitate the two-pointer technique.
2. Iterate through each element, treating it as the first element of the triplet.
3. Use two pointers to find the closest sum to the target by adjusting the pointers based on the current sum.
4. Update the closest sum whenever a closer sum is found.

### Approach 2: Brute Force Enumeration

1. Enumerate all possible triplets in the array.
2. Calculate the sum for each triplet and track the closest sum to the target.
3. Return the closest sum after evaluating all triplets.

### Approach 3: Optimized Two Pointers with Early Stopping

1. Sort the array and initialize the closest sum.
2. Use early stopping conditions to skip unnecessary calculations.
3. For each element, use two pointers to find the closest sum.
4. Return the closest sum when an exact match is found or after all elements are processed.

## 4. Code (with Key Explanations)

### Approach 1: Two Pointers with Sorting

```python
"""
Approach 1: Two Pointers with Sorting
- Sort the array and use two pointers to find the closest sum.
- Adjust pointers based on comparison with the target.
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[:3])  # Initialize to the sum of the first three elements
        min_diff = abs(closest_sum - target)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum

                if curr_sum == target:
                    return target  # Perfect match
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
```

### Approach 2: Brute Force Enumeration

```python
"""
Approach 2: Brute Force Enumeration
- Check all possible triplets and calculate their sums.
- Track the closest sum to the target.
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest_sum = float('inf')
        min_diff = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    curr_sum = nums[i] + nums[j] + nums[k]
                    diff = abs(curr_sum - target)

                    if diff < min_diff:
                        min_diff = diff
                        closest_sum = curr_sum

        return closest_sum
```

### Approach 3: Optimized Two Pointers with Early Stopping

```python
"""
Approach 3: Optimized Two Pointers with Early Stopping
- Use early stopping conditions to optimize the two-pointer approach.
- Skip unnecessary calculations when bounds exceed the target.
"""
from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[:3])
        min_diff = abs(closest_sum - target)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            min_possible = nums[i] + nums[i + 1] + nums[i + 2]
            if min_possible > target and abs(min_possible - target) < min_diff:
                return min_possible

            max_possible = nums[i] + nums[n - 2] + nums[n - 1]
            if max_possible < target and abs(max_possible - target) < min_diff:
                closest_sum = max_possible
                min_diff = abs(max_possible - target)
                continue

            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum

                if curr_sum == target:
                    return target
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
```

## 5. Test Cases

Use a Markdown table to provide at least 5 representative test cases.

| Case Description      | Input                   | Output | Explanation                                     |
|-----------------------|-------------------------|--------|-------------------------------------------------|
| Small positive values | `[1, 2, 3, 4]`, `6`     | `6`    | Exact match found with `[1, 2, 3]`.             |
| Negative values       | `[-1, -2, -3, -4]`, `-5`| `-6`   | Closest sum is `-6` with `[-1, -2, -3]`.        |
| Mixed values          | `[-1, 2, 1, -4]`, `1`   | `2`    | Closest sum is `2` with `[-1, 2, 1]`.           |
| Large list            | `[0, 0, 0, 0, 0]`, `1`  | `0`    | Only possible sum is `0`.                       |
| Edge case             | `[1, 1, 1, 1]`, `3`     | `3`    | Exact match found with `[1, 1, 1]`.             |

## 6. Complexity

Use a Markdown table to analyze the time and space complexity.

| Approach                              | Time Complexity | Space Complexity                               |
|---------------------------------------|-----------------|-----------------------------------------------|
| Two Pointers with Sorting             | O(n^2)          | O(1), only constant space for pointers.       |
| Brute Force Enumeration               | O(n^3)          | O(1), no additional space required.           |
| Optimized Two Pointers with Early Stopping | O(n^2)         | O(1), only constant space for pointers.       |

## 7. Follow-Up & Optimizations

Propose 2-3 insightful follow-up questions or optimization directions.

1. **How to handle streaming data?**  
   Consider using a sliding window approach or maintaining a dynamic list of closest sums as new data arrives.

2. **What if you need to find the closest sum for multiple targets efficiently?**  
   Investigate a precomputation strategy or use advanced data structures to quickly adjust sums for different targets.

3. **Can the algorithm be parallelized for large datasets?**  
   Explore dividing the dataset into chunks and processing them concurrently to improve performance on multi-core systems.