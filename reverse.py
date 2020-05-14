#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/18
# @Name: reverse

# 我的算法
def reverse(x):
    if x == 0:
        return 0
    str_x = str(x)
    x_s = ""
    if str_x[0] == "-":
        x_s += "-"
    x_s += str_x[::-1].lstrip("0").rstrip("-")
    x_s_i = int(x_s)
    if -2 ** 31 < x_s_i < 2 ** 31:
        return x_s_i
    else:
        return 0


# 耗时最短
def reverse_Time(x):
    res = 0
    news = abs(x)

    while news != 0:
        temp = news % 10
        res = res * 10 + temp
        news = news // 10
    if x < 0:
        if -res < -2 ** 31:
            return 0
        else:
            return -res
    else:
        if res > 2 ** 31 - 1:
            return 0
        else:
            return res


# 其他算法
def reverse_Time_less(x):
    x = str(x)
    if x[0] == "-":
        x = -1 * int(x[:0:-1])
    else:
        x = int(x[:0:-1])
    return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    s = -3456700
    print(reverse(s))
    print(reverse_Time(s))
    print(reverse_Time_less(s))
