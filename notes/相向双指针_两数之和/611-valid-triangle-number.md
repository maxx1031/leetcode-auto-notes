# Valid Triangle Number

## 1. Clarifying Questions

What boundary conditions or constraints should I confirm with an interviewer before coding? (Provide at least 3 valuable questions with typical answers).

Q: **What is the range of values for the elements in the input list?**
→ Typical Answer: The elements are non-negative integers, and their values can range from 0 to a large number, potentially up to 10^9.

Q: **What is the maximum length of the input list?**
→ Typical Answer: The length of the input list can be up to 1000 elements.

Q: **Can the input list contain duplicate values?**
→ Typical Answer: Yes, the list can contain duplicate values, which should be treated as valid candidates for forming triangles.

## 2. Algorithm & Data Structure

Briefly list the multiple core algorithmic approaches and required data structures to solve this problem.

**Main Algorithm Category:** Two Pointers

- **Approach 1 Name:** Two Pointers after Sorting
- **Approach 2 Name:** Brute Force Triplet Check
- **Approach 3 Name:** Binary Search Optimization

**Data Structure:** Array

## 3. High-Level Description

Briefly describe the execution flow for each major approach. Use "Approach X: [Approach Name]" as a title.

### Approach 1: Two Pointers after Sorting
- Sort the array to ensure any triplet `a <= b <= c`.
- Iterate over each possible third side `c` in descending order.
- Use two pointers `i` and `j` to find valid pairs `(a, b)` such that `a + b > c`.
- Increase the count based on valid pairs found.

### Approach 2: Brute Force Triplet Check
- Iterate over all possible triplets `(a, b, c)` using three nested loops.
- Check if the triplet satisfies the triangle inequality conditions `a + b > c`, `a + c > b`, `b + c > a`.
- Count valid triplets.

### Approach 3: Binary Search Optimization
- Sort the array.
- For each pair `(a, b)`, use binary search to find the largest `c` such that `a + b > c`.
- Count valid triplets using the binary search result.

## 4. Code (with Key Explanations)

### Approach 1: Two Pointers after Sorting

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Approach 1: Two Pointers after Sorting
        - Sort the array to simplify the inequality checks.
        - Use two pointers to efficiently count valid triplets.
        """
        nums.sort()
        n = len(nums)
        count = 0

        for k in range(n - 1, 1, -1):  # Fixed third side
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:  # Valid triangle
                    count += (j - i)  # All pairs (i, j-1) with j, k are valid
                    j -= 1
                else:
                    i += 1
        return count
```

### Approach 2: Brute Force Triplet Check

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Approach 2: Brute Force Triplet Check
        - Check all combinations of triplets using nested loops.
        - Verify triangle inequalities for each triplet.
        """
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        count += 1
        return count
```

### Approach 3: Binary Search Optimization

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Approach 3: Binary Search Optimization
        - Use binary search to efficiently find the valid third side.
        """
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                left, right = j + 1, n
                target = nums[i] + nums[j]
                while left < right:
                    mid = left + (right - left) // 2
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                count += left - (j + 1)
        return count
```

## 5. Test Cases

| Case Description          | Input               | Output | Explanation                                      |
|---------------------------|---------------------|--------|--------------------------------------------------|
| Normal case               | [2, 2, 3, 4]        | 3      | Three valid triangles: (2, 3, 4), (2, 2, 3), (2, 3, 4) |
| Edge case, no triangle    | [1, 2, 3]           | 0      | No valid triangle can be formed                  |
| All elements same         | [2, 2, 2]           | 1      | One valid triangle: (2, 2, 2)                    |
| Large input with duplicates | [5, 5, 5, 5, 5]    | 10     | Multiple valid triangles due to duplicates       |
| Single element            | [5]                 | 0      | Cannot form a triangle with less than 3 sides    |

## 6. Complexity

| Approach                  | Time Complexity | Space Complexity       |
|---------------------------|-----------------|------------------------|
| Two Pointers after Sorting| O(n^2)          | O(1), only sorting space |
| Brute Force Triplet Check | O(n^3)          | O(1)                   |
| Binary Search Optimization| O(n^2 log n)    | O(1), only sorting space |

## 7. Follow-Up & Optimizations

- **Handling Streaming Data:** How can the algorithm be adapted to handle streaming data, where new numbers are continuously added to the list?
- **Parallel Processing:** Explore how the problem can be solved using parallel processing to speed up the computation for very large inputs.
- **Advanced Data Structures:** Investigate using advanced data structures like segment trees or Fenwick trees to optimize the search for valid triangles further.