#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2019/11/2
# @Name: FizzBuzz


# 我的算法
def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            result.append("Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    print(fizzBuzz(15))
