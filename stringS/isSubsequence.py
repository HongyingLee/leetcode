#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/4
# @Name: isSubsequence

def isSubsequence(s,t):
    p = q = 0
    res = 0
    while p < len(t) and q < len(s):
        if t[p] == s[q]:
            res += 1
            q += 1
        p += 1
    return res == len(s)


def isSubsequence_Time(s,t):
    l = -1
    for i in s:
        l = t.find(i,l + 1)
        if l == -1:
            return False
    return True


if __name__ == '__main__':
    print(isSubsequence("a", "c"))
    print(isSubsequence_Time("a", "c"))
