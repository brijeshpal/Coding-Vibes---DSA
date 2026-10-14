class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check whether a valid number is possible
        if sum > 9 * num:
            return ""

        remaining = sum
        answer = []

        for _ in range(num):
            digit = min(9, remaining)

            answer.append(str(digit))
            remaining -= digit

        return "".join(answer)
        