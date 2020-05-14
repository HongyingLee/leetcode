#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/27
# @Name: longestCommonPrefix

# 抄的算法
def longestCommonPrefix(strs):
    a = 0
    num = []
    len_strs = len(strs)
    for i in strs:
        num.append(len(i))
    min_num = min(num)
    for i in range(min_num):
        for j in range(len_strs - 1):
            if strs[j][i] != strs[j + 1][i]:
                break
        else:
            a += 1
            continue
        break
    return strs[0][:a]


if __name__ == "__main__":
    st = ["flower", "flow", "flight"]
    print(longestCommonPrefix(st))
