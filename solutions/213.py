from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            return dp[-1]
        
        # Case 1: rob from house 0 to n-2
        # Case 2: rob from house 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


    # # 198. 打家劫舍
    # def rob1(self, nums: List[int]) -> int:
    #     f0 = f1 = 0
    #     for x in nums:
    #         f0, f1 = f1, max(f1, f0 + x)
    #     return f1

    # def rob(self, nums: List[int]) -> int:
    #     return max(nums[0] + self.rob1(nums[2:-1]), self.rob1(nums[1:]))


