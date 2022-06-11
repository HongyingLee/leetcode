#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/11
# @Name: removeElement


def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


def removeElement_Time(nums, val):
    ret = 0
    for i in nums:
        if i != val:
            nums[ret] = i
            ret += 1
    return ret


if __name__ == '__main__':
    num = [3, 2, 2, 3]
    va = 2
    print(removeElement(num, va))
    print(removeElement_Time(num, va))
