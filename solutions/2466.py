class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """
        MOD = 1_000_000_007
        @cache 
        def dfs(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            return (dfs(i-zero) + dfs(i-one)) % MOD 
        return sum(dfs(i) for i in range(low, high+1)) % MOD

# method2 
class Solution:
    
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """
        string len: [low, high]
        1 recursive method:
        for str_len in low: high:
            there are 3 types: add only 1 or only 0 or both but it depends on the length is enough
            dfs(low-one, high-one, zero, one) + dfs(low-zero, high-zero, zero, one) + dfs(low-zero-one, high-zero-one, zero, one)
        base case:
            if low >= 0 and high <= 0:
                return 1
    
        """
        # dp[i]: number of good string of exactly length i
        MOD = 10 ** 9 + 7# avoid overflow 
        dp = [1] + [0] * (high)

        for i in range(1, high+1):
            ways = 0
            if i >= zero:
                ways += dp[i-zero] 
            
            if i >= one:
                ways += dp[i-one]
            dp[i] = ways % MOD
        res = 0
        for j in range(low, high+1):
            res = (res + dp[j]) % MOD
        return res 

