
class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        nums.sort()

        n = len(nums)
        median = nums[n // 2]

        moves = 0

        for num in nums:
            moves += abs(num - median)

        return moves
