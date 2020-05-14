#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/24
# @Name: isPalindrome


# 我的算法
def isPalindrome(s):
    s_lower = s.lower()
    length = len(s_lower)
    s_l = []
    if length == 0:
        return True
    else:
        for i in range(length):
            if s_lower[i].isalpha() or s_lower[i].isdigit():
                s_l.append(s_lower[i])
        if s_l == s_l[::-1]:
            return True
        else:
            return False

# 耗时最短
def isPalindrome_Time(s):
    s1 = [*filter(str.isalnum, s.lower())]
    return s1 == s1[::-1]


if __name__ == "__main__":
    x = "A man, a plan, a canal: Panama"
    print(isPalindrome(x))
    print(isPalindrome_Time(x))
