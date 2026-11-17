
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        n = len(s)
        INF = float('inf')

        cost = [[INF] * n for _ in range(n)]

        for left in range(n):

            for right in range(left + 1, n):

                length = right - left + 1
                best = INF

                for d in range(1, length):

                    if length % d != 0:
                        continue

                    group_length = length // d
                    changes = 0

                    for offset in range(d):

                        for t in range(group_length // 2):

                            a = left + offset + t * d

                            b = left + offset + (
                                group_length - 1 - t
                            ) * d

                            if s[a] != s[b]:
                                changes += 1

                    best = min(best, changes)

                cost[left][right] = best


        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for g in range(1, k + 1):

            for i in range(2 * g, n + 1):

                for j in range(2 * (g - 1), i - 1):

                    dp[g][i] = min(
                        dp[g][i],
                        dp[g - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
