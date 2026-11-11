
class Solution:
    def minimumCost(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int
    ) -> int:

        common = min(need1, need2)

        extra1 = need1 - common
        extra2 = need2 - common

        answer = (
            common * min(costBoth, cost1 + cost2)
            + extra1 * min(cost1, costBoth)
            + extra2 * min(cost2, costBoth)
        )

        return answer
