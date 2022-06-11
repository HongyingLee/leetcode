#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/15
# @Name: majorityElement

import collections
def majorityElement_New(nums):
    n = collections.Counter(nums).most_common(1)
    return n[0][0]


def majorityElement_Sort(nums):
    nums.sort()
    return nums[len(nums) // 2]


if __name__ == '__main__':
    l = [1, 2, 1, 2, 2]
    # print(majorityElement(l))
    print(majorityElement_New(l))
    print(majorityElement_Sort(l))
