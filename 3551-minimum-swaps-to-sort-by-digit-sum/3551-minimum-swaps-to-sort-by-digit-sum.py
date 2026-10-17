class Solution:
    def minSwaps(self, nums: list[int]) -> int:

        def digit_sum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        n = len(nums)

        target = sorted(
            nums,
            key=lambda x: (digit_sum(x), x)
        )

        target_index = {
            value: index
            for index, value in enumerate(target)
        }

        permutation = [
            target_index[value]
            for value in nums
        ]

        visited = [False] * n
        swaps = 0

        for i in range(n):

            if visited[i]:
                continue

            cycle_length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                cycle_length += 1
                j = permutation[j]

            if cycle_length > 1:
                swaps += cycle_length - 1

        return swaps