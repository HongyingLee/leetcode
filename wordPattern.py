#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/24
# @Name: wordPattern


def wordPattern(pattern,s):
    dic_p = {}
    dic_s = {}
    s_l = s.strip().split(" ")

    if len(s_l) != len(pattern):
        return False

    for i in range(len(pattern)):
        if pattern[i] not in dic_p and s_l[i] not in dic_s:
            dic_p[pattern[i]] = i
            dic_s[s_l[i]] = i
        elif dic_p.get(pattern[i]) is None or dic_s.get(s_l[i]) is None:
            return False
        elif dic_p.get(pattern[i]) != dic_s.get(s_l[i]):
            return False
    return True


if __name__ == '__main__':
    pa = "aaaa"
    s1 = "cat cat cat cat"
    print(wordPattern(pa,s1))
