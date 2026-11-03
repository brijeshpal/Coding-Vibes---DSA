
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maximum = max(nums)

        return len(nums) * maximum - sum(nums)
