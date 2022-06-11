#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/25
# @Name: strStr


# 我的算法
def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    elif len(needle) > len(haystack):
        return -1
    # elif len(needle) == len(haystack) and needle == haystack:
    #     return 0
    else:
        x = haystack.find(needle)
        if x >= 0:
            return x
        else:
            return -1

# 耗时最短
def strStr_Time(haystack, needle):
    m, n = len(haystack), len(needle)
    if n == 0:
        return 0
    elif n > m:
        return -1
    for i in range(m - n + 1):
        if haystack[i] == needle[0]:
            if haystack[i:i+n] == needle:
                return i
            else:
                continue
    return -1


# 内存消耗最少
def strStr_Memo(haystack, needle):
    return haystack.find(needle)


if __name__ == "__main__":
    hay = "aaa"
    need = "aaa"
    print(strStr(hay, need))
    print(strStr_Time(hay, need))
    print(strStr_Memo(hay, need))
