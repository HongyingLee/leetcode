#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/9
# @Name: rotate


def rotate(nums, k):
    length = len(nums)
    nums[:] = nums[length - k:] + nums[:length - k]
    return nums


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    n = 3
    print(rotate(x, n))
