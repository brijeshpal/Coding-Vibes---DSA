from collections import deque

class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        INF = 10**18

        next_node = [{}]
        fail = [0]
        output = [[]]

        best = {}

        for word, cost in zip(words, costs):
            if word not in best or cost < best[word]:
                best[word] = cost

        for word, cost in best.items():
            node = 0

            for ch in word:
                if ch not in next_node[node]:
                    next_node[node][ch] = len(next_node)
                    next_node.append({})
                    fail.append(0)
                    output.append([])

                node = next_node[node][ch]

            output[node].append((len(word), cost))

        q = deque()

        for ch, node in next_node[0].items():
            q.append(node)
            fail[node] = 0

        while q:
            u = q.popleft()

            for ch, v in next_node[u].items():
                q.append(v)

                f = fail[u]

                while f and ch not in next_node[f]:
                    f = fail[f]

                if ch in next_node[f]:
                    fail[v] = next_node[f][ch]
                else:
                    fail[v] = 0

                output[v].extend(output[fail[v]])

        n = len(target)
        dp = [INF] * (n + 1)
        dp[0] = 0

        node = 0

        for i, ch in enumerate(target):
            while node and ch not in next_node[node]:
                node = fail[node]

            if ch in next_node[node]:
                node = next_node[node][ch]
            else:
                node = 0

            for length, cost in output[node]:
                start = i + 1 - length

                if dp[start] != INF:
                    dp[i + 1] = min(
                        dp[i + 1],
                        dp[start] + cost
                    )

        return -1 if dp[n] == INF else dp[n]