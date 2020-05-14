#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/4
# @Name: removeDuplicates

# 抄的算法
def removeDuplicates(nums):
    low = 0
    length = len(nums)
    if length <= 1:
        return length
    else:
        for high in range(length):
            if nums[low] < nums[high]:
                low += 1
                nums[low] = nums[high]
        return low + 1

