#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/10
# @Name: searchInsert


def searchInsert(nums, target):
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    elif target not in nums and nums[-1] > target:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
    else:
        return len(nums)


if __name__ == '__main__':
    num = [1, 3, 5, 7]
    print(searchInsert(num, 3))
    print(searchInsert(num, 2))
    print(searchInsert(num, 9))
