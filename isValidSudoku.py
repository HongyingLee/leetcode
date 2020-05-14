#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Hongying_Lee
# @Time: 2020/3/11
# @Name: isValidSudoku


def isValidSudoku(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                # 行判断
                for row in range(len(board[i])):
                    if row != i and board[row][j] == board[i][j]:
                        return False

                # 列判断
                for col in range(len(board[i])):
                    if col != j and board[i][col] == board[i][j]:
                        return False

                # 3*3矩形判断
                for row in range((i // 3) * 3, (i // 3) * 3 + 3):
                    for col in range((j // 3), (j // 3) + 3):
                        if row != i and col != j and board[row][col] == board[row][col]:
                            return False
    return True



