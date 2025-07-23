"""
0-1背包
df(i, j)表示nums[0]到nums[j]元素和等于j（target=j)的序列最长长度
- if exist return value
- if not return -inf

consider select nums[i] or not:
- no: dfs(i-1, j)
- yes: dfs(i-1, j-nums[i])

dfs(i,j) = max(dfs(i-1, j), dfs(i-1, j-nums[i]) + 1)

boundary:
- dfs(-1, 0) = 0
- dfs(-1, j) = -inf 

entrance:
- dfs(n-1, target)
"""

class Solution:
    # method1: recursion
    def lengthOfLongestSubsequence(self, nums):
        @cache 
        def dfs(i, j):
            if i < 0:
                return 0 if j == 0 else -inf 
            if nums[i] > j:
                return dfs(i-1, j) # not choose nums[i]
            return max(dfs(i-1, j), dfs(i-1, j-nums[i]) + 1)
        
        ans = dfs(len(nums)-1, target)
        dfs.cache_clear()
        return ans if ans > 0 else -1 
    # method2 dp(bottom-to-top)
    def lengthOfLongestSubsequence(self, nums):
        # f[i+1][j] = max(f[i][j], f[i][j-nums[i]+1])
        n = len(nums)
        f = [[-inf] * (target+1) for _ in range(n+1)]
        f[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(target + 1):
                if j < x:
                    f[i+1][j] = f[i][j]
                else:
                    f[i+1][j] = max(f[i][j], f[i][j-x]+1)
        return f[n][-1] if f[n][-1] > 0 else -1
    

    


