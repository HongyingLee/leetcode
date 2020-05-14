#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/4
# @Name: findTheDifference


def findTheDifference(s,t):
    dict_s = {}
    for i in s:
        if i not in dict_s:
            dict_s[i] = 1
        else:
            dict_s[i] += 1

    dict_t = {}
    for j in t:
        if j not in dict_t:
            dict_t[j] = 1
        else:
            dict_t[j] += 1

    for k in t:
        if k not in dict_s or dict_s[k] != dict_t[k]:
            return k


if __name__ == '__main__':
    print(findTheDifference("aaa", "aaab"))
