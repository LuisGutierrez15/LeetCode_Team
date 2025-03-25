from typing import List


def maxProfit(prices: List[int]) -> int:
    n: int = len(prices)

    if n < 2:
        return 0

    max_profit_left: List[int] = [0] * n  # [0,0,0,0,0... n]
    min_val: int = prices[0]

    # best time to buy
    for i in range(1, n, 1):
        min_val = min(min_val, prices[i])
        max_profit_left[i] = max(max_profit_left[i - 1], (prices[i] - min_val))

    # best time to sell
    max_profit_rigth: List[int] = [0] * n
    max_val: int = prices[-1]
    for i in range(n - 1, 0, -1):
        max_val = max(max_val, prices[i])
        max_profit_rigth[i] = max(max_profit_rigth[i - 1], (max_val - prices[i]))

    best_profit: int = 0
    for i in range(n):
        best_profit = max(best_profit, (max_profit_left[i] + max_profit_rigth[i]))

    return best_profit


p = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfit(p))
