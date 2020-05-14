#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/12
# @Name: lengthOfLastWord


def lengthOfLastWord(s):
    mid = s.strip().split(" ")
    return len(mid[-1])


if __name__ == '__main__':
    st = "hello world"
    print(lengthOfLastWord(st))
