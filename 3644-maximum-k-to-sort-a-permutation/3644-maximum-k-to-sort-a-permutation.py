class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        n = len(nums)

        if all(nums[i] == i for i in range(n)):
            return 0

        answer = None

        for i, value in enumerate(nums):
            if value != i:
                if answer is None:
                    answer = value
                else:
                    answer &= value

        return answer