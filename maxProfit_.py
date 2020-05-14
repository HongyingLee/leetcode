#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/30
# @Name: maxProfit_


# 我的算法，时间复杂度是n ** 2
def maxProfit(prices):
    sum = 0
    length = len(prices)
    for i in range(length):
        for j in range(i + 1, length):
            if prices[j] - prices[i] > sum:
                sum = prices[j] - prices[i]
            continue
        continue
    return sum


# 抄的算法
def maxProfit_Chao(prices):
    if len(prices) < 2:
        return 0
    else:
        min_price = prices[0]
        max_profite = 0
        for i in prices:
            min_price = min(min_price, i)
            max_profite = max(max_profite, i - min_price)
        return max_profite


# 耗时最短
def maxProfit_Time(prices):
    min_index = 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[min_index] > prices[i]:
            min_index = i
        else:
            if prices[i] - prices[min_index] > max_profit:
                max_profit = prices[i] - prices[min_index]
    return max_profit


if __name__ == '__main__':
    price = [7, 1, 5, 3, 6, 4]
    print(maxProfit(price))
    print(maxProfit_Chao(price))
    print(maxProfit_Time(price))
