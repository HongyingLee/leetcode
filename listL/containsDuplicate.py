#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/11/2
# @Name: containsDuplicate


def containDup(nums):
    length = len(nums)
    length_set = len(set(nums))
    if length == length_set:
        return False
    else:
        return True


def containduplicate(nums):
    ret = 0
    for i in nums:
        ret ^= i
    return ret


if __name__ == "__main__":
    x = [2, 2, 1]
    print(containduplicate(x))
    print(containDup(x))
