#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/8/29
# @Name: bubble_sort

"""
冒泡排序
每个数都和它右侧的数比较，若当前数大于右侧的数，则交换位置；否则，保持不变；
"""


def bubble_sort(sort_list):
    length = len(sort_list)
    for i in range(length - 1):
        for j in range(length - 1):
            if sort_list[j] > sort_list[j + 1]:
                sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
    return sort_list


def bubble_sort_better(sort_list):
    length = len(sort_list)
    for index in range(length - 1):
        for j in range(1, length - index):
            if sort_list[j - 1] > sort_list[j]:
                sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]
    return sort_list


if __name__ == "__main__":
    sort_list_1 = [7, 3, 5, 2, 1, 6, 4]
    print(bubble_sort(sort_list_1))
    print(bubble_sort_better(sort_list_1))
