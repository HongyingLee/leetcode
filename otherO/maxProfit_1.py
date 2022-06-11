def maxProfit(prices):
    if len(prices) <= 1:
        return 0
    min_price = min(prices)
    print(min_price)
    max_profit = 0
    print("0000:{}".format(prices.index(min_price)))
    for i in range(prices.index(prices[min_price]), len(prices)):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit


if __name__ == "__main__":
    l = [7, 6, 4, 3, 1]
    print(maxProfit(l))
