# 数组，多少对数据之和是60的倍数；

def res(nums):
    n = len(nums)
    res_l = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            total = nums[i] + nums[j]
            if total % 60 == 0:
                res_l.append((i,j))
    return len(res_l)
    key:value
    [2,2,58,58,3,3,3,57,57,57]
    {2:2,}

if __name__ == '__main__':
    #[2,2,58,58] 4
    pass