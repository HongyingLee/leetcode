#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/8/29
# @Name: TwoSum

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 链接：https://leetcode-cn.com/problems/two-sum


def two_sum(nums, target):
    for i in range(len(nums)):
        x = target - nums[i]
        if x in nums:
            j = nums.index(x)
            if i != j:
                return i, j
            else:
                continue

def twoNum(nums,target):
    hashtable = {}
    for i,num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num],i]
        hashtable[num] = i
    return []


if __name__ == "__main__":
    num = [1, 3, 5, 7, 9]
    targ = 10
    print(two_sum(num, targ))
    print(twoNum(num,targ))
