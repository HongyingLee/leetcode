#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/11
# @Name: findDisappearedNumbers


def findDisappearedNumbers(nums):
    if len(nums) == 0:
        return []
    res = []
    for i in range(1, max(max(nums), len(nums) + 1)):
        if i not in nums:
            res.append(i)
    return res

def findDisappearedNumbers_Time(nums):
    a = set(nums)
    b = set(range(1, max(max(nums), len(nums) + 1)))
    return list(a ^ b)


if __name__ == '__main__':
    print(findDisappearedNumbers([1, 1, 2]))
    print(findDisappearedNumbers_Time([1, 1, 2]))
