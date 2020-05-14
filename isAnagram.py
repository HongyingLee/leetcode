#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/16
# @Name: isAnagram


# 我的算法
def isAnagram(s, t):
    s_d = {}
    t_d = {}
    for i in s:
        if i not in s_d:
            s_d[i] = 1
        else:
            s_d[i] += 1
    for j in t:
        if j not in t_d:
            t_d[j] = 1
        else:
            t_d[j] += 1
    if s_d == t_d:
        return True
    else:
        return False


# 耗时最短
def isAnagram_Time(s,t):
    result = True
    if set(s) != set(t):
        return False
    else:
        for i in set(s):
            result = result and s.count(i) == t.count(i)
        return result


if __name__ == "__main__":
    s_1 = "abcdefg"
    t_1 = "bcdefga"
    print(isAnagram(s_1, t_1))
    print(isAnagram_Time(s_1, t_1))
