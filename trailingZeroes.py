#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/17
# @Name: trailingZeroes

def trailingZeroes(n):
    res = 0
    while n >= 5:
        n //= 5
        res += 1
    return res


if __name__ == '__main__':
    print(trailingZeroes(5))
