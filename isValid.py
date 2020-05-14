#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/4/6
# @Name: isValid


def isValid(s):
    dic = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    for i, char in enumerate(s):
        if char not in dic:
            stack.append(char)
        else:
            if not stack or stack[-1] != dic[char]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == '__main__':
    s = "(){}[]"
    print(isValid(s))
