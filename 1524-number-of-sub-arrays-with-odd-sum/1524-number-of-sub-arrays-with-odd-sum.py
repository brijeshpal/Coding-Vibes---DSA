
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        MOD = 10**9 + 7

        even_count = 1
        odd_count = 0

        prefix = 0
        answer = 0

        for num in arr:

            prefix += num

            if prefix % 2 == 1:

                answer += even_count
                odd_count += 1

            else:

                answer += odd_count
                even_count += 1

            answer %= MOD

        return answer
