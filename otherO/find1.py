# -*- coding:utf-8 -*-
def NumberOf1Between1AndN_Solution(n):
    y = 0
    for i in range(1, n + 1):
        y += find1(i)
    return y

def find1(x):
    res = 0
    charX = str(x)
    n = len(charX)
    for i in range(n):
        if charX[i] == '1':
            res += 1
    return res


if __name__ == "__main__":
    print(NumberOf1Between1AndN_Solution(13))

