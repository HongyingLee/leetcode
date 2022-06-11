#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/20
# @Name: isIsomorphic


def isIsomorphic(s,t):
    dic_s = {}
    dic_t = {}
    for i in range(len(s)):
        if s[i] not in dic_s and t[i] not in dic_t:
            dic_s[s[i]] = i
            dic_t[t[i]] = i
        elif dic_s.get(s[i]) is None or dic_t.get(t[i]) is None:
            return False
        elif dic_s.get(s[i]) != dic_t.get(t[i]):
            return False
    return True


if __name__ == '__main__':
    s1 = "eggee"
    s2 = "addav"
    print(isIsomorphic(s1, s2))
