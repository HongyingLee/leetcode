#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/23
# @Name: isUgly

def isUgly(num):
    if num <= 0:
        return False
    elif num == 1:
        return True
    else:
        while num != 1:
            if num % 5 == 0:
                num //= 5
            elif num  % 3 == 0:
                num //= 3
            elif num % 2 == 0:
                num //= 2
            else:
                return False
        return  True


if __name__ == '__main__':
    print(isUgly(14))
