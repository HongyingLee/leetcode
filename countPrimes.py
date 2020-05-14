#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/21
# @Name: countPrimes


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

