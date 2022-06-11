#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/3
# @Name: hammingWeight

# 抄的算法
def hammingWeight(n):
    result = 0
    while n:
        if 1 & n:
            result += 1
        n = n >> 1
    return result


