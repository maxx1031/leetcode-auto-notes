MOD = 1_000_000_007
f = [1, 1, 2, 4]
g = [1, 1, 2, 4]
for _ in range(10 ** 5 - 3):  # 预处理所有长度的结果
    f.append((f[-1] + f[-2] + f[-3]) % MOD)
    g.append((g[-1] + g[-2] + g[-3] + g[-4]) % MOD)

class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        """
        :type pressedKeys: str
        :rtype: int

        本质上是爬楼梯，每次可以跳1/2/3或者1/2/3/4，计算跳cnt个台阶的方案数，其中cnt表示连续相同子串的长度
        dp[i]=dp[i−1]+dp[i−2]+dp[i−3] if number is not 7 or 9
        dp[k] to mean the number of ways to interpret k identical key presses
        else 
        dp[i]=dp[i−1]+dp[i−2]+dp[i−3]+dp[i−4]
        """
        ans = 1
        for ch, s in groupby(pressedKeys):
            l = len(list(s))
            ans *= (g[l] if ch in "79" else f[l])
        return ans


