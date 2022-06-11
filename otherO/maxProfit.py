#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/9
# @Name: maxProfit

def maxProfit(prices):
    sum = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            sum += prices[i + 1] - prices[i]
    return sum


if __name__ == "__main__":
    x = [7, 1, 5, 3, 6, 4]
    print(maxProfit(x))
