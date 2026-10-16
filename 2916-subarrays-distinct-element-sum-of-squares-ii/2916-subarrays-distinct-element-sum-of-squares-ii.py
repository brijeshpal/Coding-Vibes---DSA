class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, delta):
            length = right - left + 1

            squares[node] = (
                squares[node]
                + 2 * delta * total[node]
                + delta * delta * length
            ) % MOD

            total[node] = (
                total[node] + delta * length
            ) % MOD

            lazy[node] = (lazy[node] + delta) % MOD

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            delta = lazy[node]

            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)

            mid = (left + right) // 2

            if ql <= mid:
                update(
                    node * 2, left, mid, ql, qr
                )

            if qr > mid:
                update(
                    node * 2 + 1, mid + 1, right, ql, qr
                )

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, value in enumerate(nums):
            previous = last_seen.get(value, -1)
            update(1, 0, n - 1, previous + 1, i)

            last_seen[value] = i

            answer = (answer + squares[1]) % MOD

        return answer