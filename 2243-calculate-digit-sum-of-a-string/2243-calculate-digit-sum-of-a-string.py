
class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:

            groups = []

            for i in range(0, len(s), k):

                group = s[i:i + k]

                total = 0

                for ch in group:
                    total += int(ch)

                groups.append(str(total))

            s = "".join(groups)

        return s
