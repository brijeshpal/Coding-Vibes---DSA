from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str):
        
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}

        while queue:

            # Process current BFS level
            level_size = len(queue)

            valid_strings = []

            for _ in range(level_size):
                current = queue.popleft()

                if is_valid(current):
                    valid_strings.append(current)

                # Generate next level only if
                # current level has no valid answer
                if not valid_strings:

                    for i in range(len(current)):

                        # We only remove parentheses
                        if current[i] not in "()":
                            continue

                        new_string = current[:i] + current[i + 1:]

                        if new_string not in visited:
                            visited.add(new_string)
                            queue.append(new_string)

            # If we found valid strings,
            # this is the minimum-removal level.
            if valid_strings:
                return valid_strings

        return [""]