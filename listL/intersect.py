#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/9
# @Name: intersect


def intersect(nums1, nums2):
    x = []
    length_1 = len(nums1)
    length_2 = len(nums2)
    if length_1 <= length_2:
        for num in nums1:
            if num in nums2:
                x.append(num)
                nums2.remove(num)
    else:
        for num in nums2:
            if num in nums1:
                x.append(num)
                nums1.remove(num)
    return x


if __name__ == "__main__":
    x_1 = [1, 2, 2, 1]
    x_2 = [2, 2]
    print(intersect(x_1, x_2))
