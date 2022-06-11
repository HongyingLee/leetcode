#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/21
# @Name: isPowerOfThree

def isPowerOfThree(n):
    if n <= 0:
        return False
    else:
        while n != 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True


if __name__ == "__main__":
    x = 45
    print(isPowerOfThree(x))
