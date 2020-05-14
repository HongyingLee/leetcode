#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/29
# @Name: merge


# 抄的算法
def merge(nums1, m, nums2, n):
    nums1[m:m + n] = nums2
    nums1.sort()
    return nums1


if __name__ == '__main__':
    list1 = [1, 2, 3, 0, 0, 0]
    list2 = [2, 5, 6]
    print(merge(list1, 3, list2, 3))
