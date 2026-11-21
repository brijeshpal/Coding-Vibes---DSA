
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for node in range(1, n):
            children[parent[node]].append(node)

        new_parent = parent[:]

        last_seen = [-1] * 26

        stack = [(0, True, -1)]

        while stack:
            node, entering, previous = stack.pop()
            char_index = ord(s[node]) - ord('a')

            if entering:
                previous = last_seen[char_index]

                if node != 0 and previous != -1:
                    new_parent[node] = previous
        
                last_seen[char_index] = node

                stack.append((node, False, previous))

                for child in reversed(children[node]):
                    stack.append((child, True, -1))

            else:

                last_seen[char_index] = previous

        new_children = [[] for _ in range(n)]

        for node in range(1, n):
            new_children[new_parent[node]].append(node)

        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            order.append(node)

            for child in new_children[node]:
                stack.append(child)

        answer = [1] * n

        for node in reversed(order):
            if node != 0:
                answer[new_parent[node]] += answer[node]

        return answer
