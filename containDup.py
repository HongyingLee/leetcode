#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/9
# @Name: containDup


def containDup(nums):
    length = len(nums)
    length_set = len(set(nums))
    if length == length_set:
        return False
    else:
        return True


if __name__ == "__main__":
    x = [3, 1]
    print(containDup(x))
