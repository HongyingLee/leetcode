#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/27
# @Name: merge


def merge(list1, list2):
    list_3 = []
    length_1 = len(list1)
    length_2 = len(list2)
    x = max(length_1, length_2)
    for i in range(x):
        n1 = list1[i % length_1]
        n2 = list2[i % length_2]
        list_3.append((n1, n2))
    return list_3


if __name__ == "__main__":
    list_1 = ["1", "2", "3"]
    list_2 = ["a", "b", "c", "d", "f"]
    print(merge(list_1, list_2))
