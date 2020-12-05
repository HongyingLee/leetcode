#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/21
# @Name: countPrimes


"""
统计所有小于非负整数 n 的质数的数量。
示例:
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


# 抄的算法
def countPrimes(n):
    if n < 2:
        return 0
    else:
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if res[i]:
                res[i * i:n:i] = [False] * len(res[i * i:n:i])
        return res.count(True)


if __name__ == "__main__":
    x = 10
    print(countPrimes(x))

