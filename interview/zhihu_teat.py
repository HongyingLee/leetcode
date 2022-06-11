# 有一个有符号的整数（-123）
#输出有符号整数的-321
#如果尾号是0，120，21

def reverseNum(num):
    str_num = str(num)
    if str_num[0] == "-":
        res_num = -1 * int(str_num[::-1].rstrip("-"))
    else:
        res_num = int(str_num[::-1])
    return res_num


if __name__ == '__main__':
    num= -123
    print(reverseNum(num))
    num1 = 120
    print(reverseNum(num1))
    num2 = 3987
    print(reverseNum(num2))
    num3 = 1200
    print(reverseNum(num3))