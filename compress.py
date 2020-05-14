#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/5/10
# @Name: compress

def compress(chars):
    dict_chars = {}
    for i in chars:
        if i not in dict_chars:
            dict_chars[i] = 1
        else:
            dict_chars[i] += 1

    res = []
    for k in dict_chars.keys():
        res.append(k)
        if 1 < dict_chars[k] < 10:
            res.append(str(dict_chars[k]))
        elif dict_chars[k] >= 10:
            x = list(str(dict_chars[k]))
            for j in range(len(x)):
                res.append(x[j])
    return res


def compress_Time(chars):
    i, j = 0, 1
    while i < len(chars) - 1:
        if chars[i] == chars[i + 1]:
            j += 1
            del chars[i + 1]
        elif chars[i] != chars[i + 1]:
            if j > 1:
                str_j = str(j)
                for c in range(len(str_j)):
                    chars.insert(i + 1 + c, str_j[c])
                i += 2
            else:
                i += 1
                j = 1

    if j > 1:
        str_j = str(j)
        for c in range(len(str_j)):
            chars.insert(i + 1 + c, str_j[c])

    print(chars)
    return len(chars)


if __name__ == '__main__':
    print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(compress_Time(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
