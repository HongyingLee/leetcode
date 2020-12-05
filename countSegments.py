#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/8
# @Name: countSegments

"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
"""


def countSegments(s):
    length = len(s)
    res = 0
    for i in range(length):
        if (i == 0 and s[0] != " ") or (s[i] != " " and s[i - 1] == " "):
            res += 1
    return res


if __name__ == '__main__':
    print(countSegments("Hello, my name is John"))
