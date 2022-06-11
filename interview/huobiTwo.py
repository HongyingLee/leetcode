# 函数，n，返回n的阶乘

def jc(n):
    res = n
    for i in range(1,n):
        res = res * i
    return res

print(jc(3))