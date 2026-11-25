
class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        length = [0]
        link = [-1]
        occ = [0]
        nxt = [{}]

        last = 0

        for x in nums:
            cur = len(length)

            length.append(length[last] + 1)
            link.append(0)
            occ.append(1)
            nxt.append({})

            p = last

            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][x]

                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(length)

                    length.append(length[p] + 1)
                    link.append(link[q])
                    occ.append(0)
                    nxt.append(nxt[q].copy())

                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]

                    link[q] = clone
                    link[cur] = clone

            last = cur

        size = len(length)
        count = [0] * (n + 1)

        for state_length in length:
            count[state_length] += 1

        for i in range(1, n + 1):
            count[i] += count[i - 1]

        order = [0] * size

        for state in range(size - 1, -1, -1):
            state_length = length[state]
            count[state_length] -= 1
            order[count[state_length]] = state

        for state in reversed(order):
            if state != 0:
                parent_state = link[state]
                occ[parent_state] += occ[state]

        answer = n

        for state in range(1, size):
            if occ[state] == 1:
                min_length = length[link[state]] + 1
                answer = min(answer, min_length)

        return answer
