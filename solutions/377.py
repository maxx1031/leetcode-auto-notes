class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        clarify:
        - input: distinct integers 
            - can data use more than once 
            
        - output: the number of path
            - permutation not combinations

        algorithm:
        - sort nums and can see it as sub-problem like:
            - we scan the nums with for-loop and call combinationSum4(nums[i:], target-nums[i])
            - the order is matter, how to deal with it  
            
        """
        # method1：recursive
        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 1
        #     count = sum(dfs(i-num) for num in nums if num <= i)
        #     return count 
        # return dfs(target)

        # method2: dynamic programming
        dp = [1] + target * [0]
        for i in range(1, target+1):
            dp[i] = sum(dp[i-num] for num in nums if num <= i)
        return dp[-1]
        



