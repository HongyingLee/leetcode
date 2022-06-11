#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/26
# @Name: countAndSay

"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1. 1
2. 11
3. 21
4. 1211
5. 111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。

示例 1:
输入: 1
输出: "1"
解释：这是一个基本样例。
示例 2:
输入: 4
输出: "1211"
解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 "1" 可以读作 "11"。所以
"""


# 抄的算法
def countAndSay(n):
    if n <= 1:
        return "1"
    prestr = countAndSay(n - 1)
    res = ""
    count = 1
    for ids in range(len(prestr)):
        if ids == 0:
            count = 1
        elif prestr[ids] != prestr[ids - 1]:
            temp =str(count) +prestr[ids - 1]
            res += temp
            count = 1
        elif prestr[ids] == prestr[ids - 1]:
            count += 1
        if ids == len(prestr) - 1:
            temp = str(count) + prestr[ids]
            res += temp
    return res


# 耗时最短
def countAndSay_Time(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"

    res = [1, 1]
    for i in range(3, n+1):
        new_res = []
        num = 1
        cur = res[0]
        for s in res[1:]:
            if s == cur:
                num += 1
            else:
                new_res.append(num)
                new_res.append(cur)
                num = 1
                cur = s
        new_res.append(num)
        new_res.append(cur)
        res = new_res
    return "".join(list(map(str, res)))


# 内存占用最少
from itertools import groupby
def countAndsay_Memo(n):
    result = "1"
    for i in range(1, n):
        result = "".join([str(len(list(g))) + k for k, g in groupby(result)])
    return result


if __name__ == "__main__":
    n = 5
    print(countAndSay(5))
    print(countAndSay_Time(n))
    print(countAndsay_Memo(5))
