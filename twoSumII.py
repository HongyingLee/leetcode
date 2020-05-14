#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/9
# @Name: twoSumII


def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i + 1, j + 1


# 双指针
def twoSumII(numbers, target):
    left,right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return left + 1, right + 1


if __name__ == '__main__':
    num = [2, 7, 10, 11]
    tar = 9
    print(twoSumII(num, tar))
