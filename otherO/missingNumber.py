#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/5
# @Name: missingNumber

# 我的算法
def missingNumber(nums):
    for i in range(len(nums) + 1):
        if i not in nums:
            return i


# 耗时最短
def missingNumber_Time(nums):
    expect = (1 + len(nums)) * len(nums) // 2
    actual = sum(nums)
    return expect - actual