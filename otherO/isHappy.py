#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/19
# @Name: isHappy


def isHappy(n):
    res_set = set()
    res_set.add(n)
    while n != 1:
        n = sum(int(i) ** 2 for i in list(str(n)))
        if n in res_set:
            return False
        else:
            res_set.add(n)
    return True


if __name__ == '__main__':
    print(isHappy(19))
