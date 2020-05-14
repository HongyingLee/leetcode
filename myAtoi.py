#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/17
# @Name: myAtoi


import re

# 我的算法
def myAtoi(s):
    if s == "" or s.strip() == "":
        return 0
    s_st = s.strip()
    pattern = re.compile(r"^[+,-]?\d+")
    result = pattern.findall(s_st)
    if len(result) == 0:
        return 0
    if int(result[0]) < -2 ** 31:
        return -2 ** 31
    elif int(result[0]) > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return int(result[0])


#耗时最短
def myAtoi_Time(s):
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)


if __name__ == "__main__":
    s = "42"
    print(myAtoi(s))
    print(myAtoi_Time(s))
