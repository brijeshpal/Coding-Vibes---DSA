
class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()

        dp = {}
        answer = 0

        for x in nums:
            dp[x + 1] = max(
                dp.get(x + 1, 0),
                dp.get(x, 0) + 1
            )

            dp[x] = max(
                dp.get(x, 0),
                dp.get(x - 1, 0) + 1
            )

            answer = max(answer, dp[x], dp[x + 1])

        return answer
