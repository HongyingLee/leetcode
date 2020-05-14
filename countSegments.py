#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/8
# @Name: countSegments

def countSegments(s):
    length = len(s)
    res = 0
    for i in range(length):
        if (i == 0 and s[0] != " ") or (s[i] != " " and s[i - 1] == " "):
            res += 1
    return res


if __name__ == '__main__':
    print(countSegments(", , , ,        a, eaefa"))
