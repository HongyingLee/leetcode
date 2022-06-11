# 输入一个字符串，输出每个字符出现的次数

def cipin(s):
    dict_res = {}

    for i in range(len(s)):
        if s[i] not in dict_res:
            dict_res[s[i]] = 1
        else:
            dict_res[s[i]] += 1
    return dict_res


# 列表，找到第二大的数

def findSecond(nums):
    n = len(nums)
    if n < 2:
        return -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums[1]


def findSecondNew(nums):
    n = len(nums)
    if n < 2:
        return -1
    sorted(nums, reverse=True)
    return nums[1]



if __name__ == '__main__':
    print(cipin("abcdabc"))
    print(findSecond([1]))
    print(findSecond([1, 5, 7]))
    print("----")
    print(findSecond([1]))
    print(findSecond([1, 5, 7]))
