
from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_factor = max(factor for factor, price in items)
        min_price = min(price for factor, price in items)

        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        multiples_count = [0] * (max_factor + 1)

        for factor in range(1, max_factor + 1):
            total = freq[factor]

            for multiple in range(factor * 2, max_factor + 1, factor):
                total += freq[multiple]

            multiples_count[factor] = total

        bonus_by_price = defaultdict(int)

        for factor, price in items:
            gain = multiples_count[factor] - 1

            if price < 2 * min_price and gain > 0:
                bonus_by_price[price] += gain

        answer = 0

        for price in sorted(bonus_by_price):
            if budget < price:
                break

            available = bonus_by_price[price]
            take = min(available, budget // price)

            answer += 2 * take
            budget -= take * price

        answer += budget // min_price

        return answer
