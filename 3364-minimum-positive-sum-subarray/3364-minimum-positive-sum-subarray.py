
class Solution:
    def minimumSumSubarray(
        self, nums: list[int], l: int, r: int
    ) -> int:

        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        answer = float('inf')
        for i in range(n):

            for length in range(l, r + 1):

                j = i + length - 1

                if j >= n:
                    break

                current_sum = prefix[j + 1] - prefix[i]

                if current_sum > 0:
                    answer = min(answer, current_sum)

        return answer if answer != float('inf') else -1
