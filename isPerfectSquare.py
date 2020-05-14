#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/30
# @Name: isPerfectSquare

def isPerfectSquare_My(num):
    for i in range(num // 2):
        if i ** 2 == num:
            return True
    return False



def isPerfectSquare(num):
    l,r = 1, num
    mid = (l + r) / 2
    while l < r:
        if mid ** 2 < num:
            l = mid + 1
        else:
            r = mid
    return l ** 2 == num


if __name__ == '__main__':
    print(isPerfectSquare(16))
