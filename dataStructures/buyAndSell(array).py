from typing import List

def maxProfit(prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # Update the minimum price if the current price is lower
            print("min_price", min_price, " max_profit", max_profit)
            min_price = min(min_price, price)

            # Update the maximum profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, price - min_price)

        return max_profit

cases = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]

for case in cases:
     print(case, maxProfit(case))