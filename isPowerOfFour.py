#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/28
# @Name: isPowerOfFour

def isPowerOfFour(num):
    if num <= 0:
        return False
    while num != 1:
        if num % 4 == 0:
            num //= 4
        else:
            return False
    return True


if __name__ == '__main__':
    print(isPowerOfFour(16))
