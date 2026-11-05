
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(
        self,
        arr1: list[int],
        arr2: list[int],
        d: int
    ) -> int:

        arr2.sort()
        count = 0

        for x in arr1:
            lower = x - d
            upper = x + d

            idx = bisect_left(arr2, lower)

            if idx == len(arr2) or arr2[idx] > upper:
                count += 1

        return count
