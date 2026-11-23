
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:

        # Reset prefix when zero arrives
        if num == 0:
            self.prefix = [1]

        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:

        # Zero is present in the last k numbers
        if k >= len(self.prefix):
            return 0

        return self.prefix[-1] // self.prefix[-k - 1]
