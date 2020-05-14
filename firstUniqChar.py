#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/15
# @Name: firstUniqChar

# 耗时最短的算法
def firstUniqChar(s):
    length = len(s)
    for ch in s:
        left = s.find(ch)
        if left != -1 and left == s.rfind(ch):
            length = min(length, left)
    return length if length != len(s) else -1


# 内存消耗最小的算法
def firstUniqChar_less(s):
    for idx, char_ in enumerate(s):
        if char_ not in s[idx + 1:] and char_ not in s[: idx]:
            return idx
        return -1


# 我的算法
def firstUniqChar_Lee(s):
    d = {}
    s_key = []
    for i in s:
        if s not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key in d:
        if d[key] == 1:
            s_key.append(s.index(key))
    # if len(s_key) == 0:
    #     return -1
    # else:
    #     return min(s_key)
    return min(s_key) if len(s_key) != 0 else -1


if __name__ == "__main__":
    char = "leetcode"
    print(firstUniqChar(char))
    print(firstUniqChar_Lee(char))
    print(firstUniqChar_less(char))
