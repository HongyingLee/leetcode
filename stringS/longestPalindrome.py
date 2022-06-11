#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/6
# @Name: longestPalindrome

def longestPalindrome(s):
    dict_s = {}
    res = 0

    for i in s:
        if i not in dict_s:
            dict_s[i] = 1
        else:
            dict_s[i] += 1

    for k in dict_s.keys():
        if dict_s[k] % 2 == 0 and dict_s[k] != 0:
            res += dict_s[k]
            dict_s[k] = 0
        elif dict_s[k] % 2 == 1:
            res += (dict_s[k] - 1)
            dict_s[k] = 1

    if 1 in dict_s.values():
        return res + 1
    else:
        return res


if __name__ == '__main__':
    print(longestPalindrome("abbcccdddd"))
