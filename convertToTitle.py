#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/14
# @Name: convertToTitle


def convertToTitle(n):
    table = [*map(chr, range(65, 91))]
    # print(table)
    if n <= 26:
        return table[n - 1]
    else:
        return convertToTitle((n - 1) // 26) + table[(n - 1) % 26]


def convertToTitle_My(n):
    dic = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
           11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T",
           21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"
           }
    res = ""
    if n <= 26:
        return dic[n]
    else:
        x = n // 26
        last = n % 26
        if last == 0:
            res = res + "Z"
            x = x - 1
        else:
            res = res + dic[last]
        while x > 26:
            x = x // 26
            last_2 = x % 26
            if last_2 == 0:
                res = res + "Z"
                x = x - 1
            else:
                res = res + dic[last_2]
        res = res + dic[x]
        return res[::-1]


if __name__ == '__main__':
    print(convertToTitle(52))
    print(convertToTitle(703))
    print(convertToTitle_My(52))
    print(convertToTitle(703))
