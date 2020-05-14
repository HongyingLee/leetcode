#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/26
# @Name: countAndSay

# 抄的算法
def countAndSay(n):
    if n <= 1:
        return "1"
    prestr = countAndSay(n - 1)
    res = ""
    count = 1
    for ids in range(len(prestr)):
        if ids == 0:
            count = 1
        elif prestr[ids] != prestr[ids - 1]:
            temp =str(count) +prestr[ids - 1]
            res += temp
            count = 1
        elif prestr[ids] == prestr[ids - 1]:
            count += 1
        if ids == len(prestr) - 1:
            temp = str(count) + prestr[ids]
            res += temp
    return res


# 耗时最短
def countAndSay_Time(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    res = [1, 1]
    for i in range(3, n+1):
        new_res = []
        num = 1
        cur = res[0]
        for s in res[1:]:
            if s == cur:
                num += 1
            else:
                new_res.append(num)
                new_res.append(cur)
                num = 1
                cur = s
        new_res.append(num)
        new_res.append(cur)
        res = new_res
    return "".join(list(map(str, res)))


# 内存占用最少
from itertools import groupby
def countAndsay_Memo(n):
    result = "1"
    for i in range(1, n):
        result = "".join([str(len(list(g))) + k for k, g in groupby(result)])
    return result


if __name__ == "__main__":
    n = 5
    print(countAndSay(5))
    print(countAndSay_Time(n))
    print(countAndsay_Memo(5))
