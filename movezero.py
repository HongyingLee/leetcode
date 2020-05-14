#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/11/2
# @Name: movezero


def movezero(nums):

    k = 0
    for i in range(len(nums)):
        if nums[i - k] == 0:
            del nums[i - k]
            nums.append(0)
            k += 1
    return nums


    # n = nums.count(0)
    # for i in range(n):
    #     nums.remove(0)
    # nums.extend([0] * n)
    #
    # return nums


if __name__ == "__main__":
    x = [0, 0, 1]
    print(movezero(x))
