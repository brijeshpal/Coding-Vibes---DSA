
class Solution:
    def palindromePath(
        self,
        n: int,
        edges: list[list[int]],
        s: str,
        queries: list[str]
    ) -> list[bool]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        chars = list(s)
        char_mask = [
            1 << (ord(c) - ord('a'))
            for c in chars
        ]

        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n

        tin = [0] * n
        tout = [0] * n
        order = []
        timer = 0

        stack = [(0, 0, False)]

        while stack:
            u, parent, exiting = stack.pop()

            if not exiting:
                tin[u] = timer
                order.append(u)
                timer += 1

                up[0][u] = parent

                for j in range(1, LOG):
                    up[j][u] = up[j - 1][up[j - 1][u]]

                stack.append((u, parent, True))

                for v in reversed(adj[u]):
                    if v != parent:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, False))
            else:
                tout[u] = timer - 1

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]
        bit = [0] * (n + 2)

        def add(i, delta):
            while i <= n:
                bit[i] ^= delta
                i += i & -i

        def range_xor(left, right, delta):
            add(left + 1, delta)
            add(right + 2, delta)

        def point_query(pos):
            i = pos + 1
            result = 0

            while i > 0:
                result ^= bit[i]
                i -= i & -i

            return result

        for u in order:
            range_xor(tin[u], tout[u], char_mask[u])

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                new_mask = 1 << (ord(new_char) - ord('a'))
                delta = char_mask[u] ^ new_mask

                if delta:
                    range_xor(tin[u], tout[u], delta)

                chars[u] = new_char
                char_mask[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                prefix_u = point_query(tin[u])
                prefix_v = point_query(tin[v])

                path_mask = (
                    prefix_u
                    ^ prefix_v
                    ^ char_mask[ancestor]
                )

                answer.append(
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer
