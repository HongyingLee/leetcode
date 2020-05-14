#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/23
# @Name: addDigits

def addDigits(num):
    while len(list(str(num))) != 1:
        num = sum(int(i) for i in list(str(num)))
    return num


if __name__ == '__main__':
    print(addDigits(12))
