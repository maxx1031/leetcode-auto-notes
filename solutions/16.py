class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        clarify question:
        1. return:
        2. invalid result
        3. duplicate values
        4. more than one result

        algorithm:
        1 convert it as three sum and use a global variable to save the closest sum value delta 
        2. how to move pointer: 
        - the 1st one: use for-loop in [0, n-2)
        - the 2nd, 3rd ones while-loop: are left and right pointer respectively, i+1, n-1
            - if abs(target - current sum_value) < abs(closest sum value delta), update and record target - current sum_value
            - elif sum < target: move 2nd to the right
            - elif sum > target: move 3rd to the left 
        3. early stopping:
            -sum(i,i+1,i+2) > target and -delta > global_delta
            -sum(i,n-2,n-1) < target and delta > global_delta
        """
        from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[:3])  # 初始化为前三个的和
        min_diff = abs(closest_sum - target)

        for i in range(n - 2):
            # 剪枝 1：跳过重复 i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 剪枝 2：early stopping
            min_possible = nums[i] + nums[i + 1] + nums[i + 2]
            if min_possible > target:
                if abs(min_possible - target) < min_diff:
                    return min_possible
                break  # 后面只会更大，直接退出

            max_possible = nums[i] + nums[n - 2] + nums[n - 1]
            if max_possible < target:
                if abs(max_possible - target) < min_diff:
                    closest_sum = max_possible
                    min_diff = abs(max_possible - target)
                continue  # 当前 i 不行，尝试下一个 i

            # 双指针部分
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(curr_sum - target)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum

                if curr_sum == target:
                    return target  # 完美匹配
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
