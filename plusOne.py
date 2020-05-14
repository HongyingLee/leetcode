#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/9
# @Name: plusOne


def plusOne(digits):
    d_i = ""
    for i in digits:
        d_i += str(i)
    d_i_1 = int(d_i) + 1
    d_i_1_l = []
    for i in str(d_i_1):
        d_i_1_l.append(int(i))
    return d_i_1_l


if __name__ == "__main__":
    x = [1, 2, 9]
    print(plusOne(x))
