
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:

        inc = 1
        dec = 1
        answer = 1

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                inc = 1

            if nums[i] < nums[i - 1]:
                dec += 1
            else:
                dec = 1

            answer = max(answer, inc, dec)

        return answer
