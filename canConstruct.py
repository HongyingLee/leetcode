#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/2
# @Name: canConstruct
"""
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

注意：
你可以假设两个字符串均只含有小写字母。
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""


def canConstruct(ransomNote, magazine):
    maga_dict = {}
    for i in magazine:
        if i not in maga_dict:
            maga_dict[i] = 1
        else:
            maga_dict[i] += 1

    for j in list(ransomNote):
        if j in maga_dict.keys() and maga_dict[j] > 0:
            maga_dict[j] -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(canConstruct("aa", "aba"))
