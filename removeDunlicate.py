#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/11/2
# @Name: removeDunlicate

def removeduplicat(nums):
    low = 0
    for high in range(len(nums)):
        if nums[low] < nums[high]:
            low += 1
            nums[low] = nums[high]
    return low + 1


if __name__ == "__main__":
    x = [1, 1, 2, 2, 3, 3, 4]
    print(removeduplicat(x))
