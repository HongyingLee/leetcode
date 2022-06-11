#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/6
# @Name: thirdMax


def thirdMax(nums):
    nums_set = sorted(set(nums), reverse=True)
    length = len(nums_set)
    if length < 3:
        return max(nums_set)
    else:
        return nums_set[2]


if __name__ == '__main__':
    print(thirdMax([1, 1, 2]))
