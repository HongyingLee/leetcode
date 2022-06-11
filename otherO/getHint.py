#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/26
# @Name: getHint


def getHint(secret, guess):
    dic_s = {}
    list_g = []
    a = 0
    b = 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            a += 1
        else:
            if secret[i] not in dic_s:
                dic_s[secret[i]] = 1
            else:
                dic_s[secret[i]] += 1
            list_g.append(guess[i])

    for i in list_g:
        if i in dic_s.keys() and dic_s[i] > 0:
            dic_s[i] -= 1
            b += 1

    res = "{0}A{1}B".format(a, b)
    return res


if __name__ == '__main__':
    s = "1122"
    g = "0001"
    print(getHint(s, g))

