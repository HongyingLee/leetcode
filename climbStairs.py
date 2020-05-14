#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/30
# @Name: climbStairs


def climbStairs(n):
    res = [0, 1, 2]
    for i in range(3, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n]


if __name__ == '__main__':
    x = 90
    print(climbStairs(x))
