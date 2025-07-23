class Solution:
    # method1 recursion
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return grid[i][j]
            return min(dfs(i, j - 1), dfs(i - 1, j)) + grid[i][j]
        return dfs(len(grid) - 1, len(grid[0]) - 1)

    # method2 2D
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                f[i + 1][j + 1] = min(f[i + 1][j], f[i][j + 1]) + x
        return f[m][n]

    # method3 1D
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        f = [inf] * (len(grid[0]) + 1)
        f[1] = 0
        for row in grid:
            for j, x in enumerate(row):
                f[j + 1] = min(f[j], f[j + 1]) + x
        return f[n]
