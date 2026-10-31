
class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        dp = [0] * n

        dp[0] = 1

        for r in range(m):
            left = 0

            for c in range(n):

                if grid[r][c] == 1:
                    left, dp[c] = dp[c], left

                else:
                    total = (left + dp[c]) % MOD

                    left = total
                    dp[c] = total

        return left
