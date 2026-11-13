
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(
        self, nums: list[int], k: int
    ) -> int:

        n = len(nums)

        dq = deque()

        cost = 0
        answer = 0

        j = n - 1

        for i in range(n - 1, -1, -1):

            num = nums[i]
            count = 1

            while dq and dq[-1][0] < num:

                next_num, next_count = dq.pop()

                count += next_count

                cost += (num - next_num) * next_count

            dq.append((num, count))

            while cost > k:

                right_num, right_count = dq.popleft()

                cost -= right_num - nums[j]

                j -= 1

                if right_count > 1:
                    dq.appendleft((right_num, right_count - 1))

            answer += j - i + 1

        return answer
