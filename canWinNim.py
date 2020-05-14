#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/25
# @Name: canWinNim


def canWinNim(n):
    if n <= 3:
        return True
    elif n % 4 != 0:
        return True
    elif n % 4 == 0:
        return False


if __name__ == '__main__':
    print(canWinNim(200))