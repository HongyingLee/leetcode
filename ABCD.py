#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/27
# @Name: ABCD

# ABCD * 4 = DCBA

#A = D * 4 % 10


def four(nums):
    res = []
    result_1 = nums[0] * 1000 + nums[1] * 100 + nums[2] * 10 + nums[3] * 1
    result_2 = nums[0] * 1000 + nums[1] * 10 + nums[2] * 100 + nums[3] * 1
    result_3 = nums[0] * 1000 + nums[1] * 10 + nums[2] * 1 + nums[3] * 100
    result_4 = nums[0] * 1000 + nums[1] * 100 + nums[2] * 1 + nums[3] * 10
    result_5 = nums[0] * 1000 + nums[1] * 1 + nums[2] * 10 + nums[3] * 100
    result_6 = nums[0] * 1000 + nums[1] * 1 + nums[2] * 100 + nums[3] * 10
    res.append(result_1)
    res.append(result_2)
    res.append(result_3)
    res.append(result_4)
    res.append(result_5)
    res.append(result_6)
    return res


def perm(n, begin, end):
    if begin >= end:
        print(n)
    else:
        i = begin
        for num in range(begin, end):
            n[num], n[i] = n[i], n[num]
            perm(n, begin + 1, end)
            n[num], n[i] = n[i], n[num]


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    perm(nums, 0, len(nums))
