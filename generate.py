#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/8
# @Name: generate


def generate(numRows):
    l1 = [1]
    l2 = []
    n = 0
    while n < numRows:
        l2.append(l1)
        l1 = [sum(t) for t in zip([0] + l1, l1 + [0])]
        n += 1
    return l2


if __name__ == '__main__':
    num = 3
    print(generate(num))
