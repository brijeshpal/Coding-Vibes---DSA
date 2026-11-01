
class Solution:
    def minMoves(self, nums: list[int]) -> int:

        minimum = min(nums)
        total = sum(nums)

        return total - len(nums) * minimum
