#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/1
# @Name: maxSubArray

# 抄的算法
def maxSubArray(nums):
    length = len(nums)
    i = 0
    sum = 0
    MaxSum = nums[0]
    while i < length:
        sum += nums[i]
        if sum > MaxSum:
            MaxSum = sum
        if sum < 0:
            sum = 0
        i += 1
    return MaxSum


if __name__ == '__main__':
    num = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(num))
