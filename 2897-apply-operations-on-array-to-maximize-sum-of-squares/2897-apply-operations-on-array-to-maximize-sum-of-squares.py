class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        MAX_BITS = 30

        # Step 1: Count set bits at every position
        bit_count = [0] * MAX_BITS

        for num in nums:
            for bit in range(MAX_BITS):
                if num & (1 << bit):
                    bit_count[bit] += 1

        # Step 2: Greedily construct k numbers
        answer = 0

        for _ in range(k):
            num = 0

            for bit in range(MAX_BITS):
                if bit_count[bit] > 0:
                    num |= (1 << bit)
                    bit_count[bit] -= 1

            # Step 3: Add the square modulo MOD
            answer = (answer + num * num) % MOD

        return answer