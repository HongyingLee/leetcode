#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/10
# @Name: moveZeroes


def moveZeroes(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i - k] == 0:
            del nums[i - k]
            nums.append(0)
            k += 1
    return nums


if __name__ == "__main__":
    x = [0, 1, 0, 3, 12]
    print(moveZeroes(x))
