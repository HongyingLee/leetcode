#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/21
# @Name: isPowerOfTwo


def isPowerOfTwo(n):
    if n <= 0:
        return False
    else:
        while n != 1:
            if n % 2 != 0:
                return False
            n /= 2
        return True


if __name__ == '__main__':
    print(isPowerOfTwo(218))
