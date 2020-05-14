#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/16
# @Name: titleToNumber


def titleToNumber(s):
    result = 0
    for i, j in enumerate(s[::-1]):
        result += 26 ** i * (ord(j) - 64)
    return result


if __name__ == '__main__':
    print(titleToNumber("AZ"))
