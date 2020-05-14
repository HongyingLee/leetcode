#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/2
# @Name: canConstruct


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
