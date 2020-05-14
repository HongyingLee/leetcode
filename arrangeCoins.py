#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/9
# @Name: arrangeCoins

def arrangeCoins(n):
    if n == 0:
        return 0
    k = 1
    while n != 0:
        if n - 2 * k >= 1:
            n -= k
            k += 1
        else:
            n = 0
    return k


if __name__ == '__main__':
    print(arrangeCoins(5))
