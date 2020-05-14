#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/29
# @Name: firstBadVersion

def isBadVersion(n):
    pass

# 依次循环遍历，找出第一个错误版本
def firstBadVersion_origin(n):
    for i in range(n + 1):
        if isBadVersion(i) == True:
            return i


# 二分查找
def firstBadVersion(n):
    left = 0
    right = n
    mid = (left + right) // 2
    while True:
        if isBadVersion(mid) == False and isBadVersion(mid + 1) == True:
            return mid + 1
        elif isBadVersion(mid) == True and isBadVersion(mid + 1) == True:
            right = mid
        elif isBadVersion(mid) == False and isBadVersion(mid + 1) == False:
            left = mid

# 耗时最短
def firstBadVersion_Time(n):
    left = 1
    right = n
    while left < right:
        mid = right + (1 - right) // 2
        if isBadVersion(mid) == True:
            right = mid
        else:
            left = mid + left
        return left
