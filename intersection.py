#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/29
# @Name: intersection


def intersection(nums1, nums2):
    length_1 = len(nums1)
    length_2 = len(nums2)
    res = []
    x = min(length_1, length_2)

    if x == length_1:
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
    else:
        for i in nums2:
            if i in nums1 and i not in res:
                res.append(i)
    return res

