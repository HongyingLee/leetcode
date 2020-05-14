#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/13
# @Name: mySqrt


def mySqrt(x):
    if x <= 0:
        return 0
    elif x <= 2:
        return 1
    for i in range(x * 0.5):
        if i * i > x:
            return i - 1,


