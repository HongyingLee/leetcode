#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/2
# @Name: rob

# 抄的算法
def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        return max(nums)
    else:
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1],dp[i - 2] + nums[i])
        return dp[len(nums) - 1]

# 耗时最短
def rob_Time(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) <= 2:
        return max(nums)
    else:
        for i in range(2, len(nums)):
            nums[i] += max(nums[: i - 1])
        return max(nums)


if __name__ == '__main__':
    x = [2, 7, 9, 3, 1]
    print(rob(x))
    print(rob_Time(x))
