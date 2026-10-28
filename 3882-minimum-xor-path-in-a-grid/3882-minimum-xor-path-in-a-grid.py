class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]

        for r in range(m):
            for c in range(n):
                value = grid[r][c]
                current = set()

                if r == 0 and c == 0:
                    current.add(value)
                else:
                    # From above
                    if r > 0:
                        for x in dp[c]:
                            current.add(x ^ value)

                    # From left
                    if c > 0:
                        for x in dp[c - 1]:
                            current.add(x ^ value)

                dp[c] = current

        return min(dp[n - 1])