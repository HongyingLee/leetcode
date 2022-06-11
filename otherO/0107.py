#!/usr/bin/python3
# -*- coding:utf-8 -*-
import requests

def yinshi(num):
    # key:和，value：(因式1，因式2)
    if num == 1:
        return 2
    res = {}
    for i in range(1, int(num/2)+1):
        j = num % i
        if j == 0:
            result = i + num / i
            res[result] = (i, num / i)
    return min(res), res[min(res)]


if __name__ == "__main__":
    # yinshi(1)
    yinshi(2)
    yinshi(3)
    yinshi(4)
    yinshi(6)
    yinshi(9)

