#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/22
# @Name: rotateImage


def rotateImage(matrix):
    n = len(matrix[0])
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i].reverse()
    return matrix


if __name__ == "__main__":
    ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotateImage(ma))
