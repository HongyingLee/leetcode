"""
最小k个数

给定一个数组，找出其中最小的K个数。例如数组元素是4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
0 <= k <= input.length <= 10000
0 <= input[i] <= 10000


输入 [4,5,1,6,2,7,3,8], 4
输出 [1,2,3,4]


输入 [1], 0
输出 []
"""


def findMixk(nums, k):
    n = len(nums)
    if n < k:
        return -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums[0:k]


"""
给定一个长度为 n 的整数数组 nums，数组中所有的数字都在 0∼n−1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
注意：如果某些数字不在 0∼n−1 的范围内，或数组中不包含重复数字，则返回 -1；给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。
"""


def findN(nums):
    n = len(nums)
    dict_r = {}
    for i in range(n):
        if nums[i] not in range(n):
            return -1
        else:
            if nums[i] not in dict_r:
                dict_r[nums[i]] = 1
            else:
                dict_r[nums[i]] += 1
    occ = set()
    for key, value in dict_r.items():
        if value not in occ:
            occ.add(value)
    if len(occ) == 1 and occ[0] == 1:
        return -1
    else:
        for key, value in dict_r.items():
            if value != 1:
                return key


if __name__ == '__main__':
    print(findMixk([4, 5, 1, 6, 2, 7, 3, 8], 4))
    print(findMixk([1], 0))

    print("-------------------")
    print(findN([2, 3, 5, 4, 3, 2, 6, 7]))
    print(findN([1, 3]))
    print(findN([1, 2, 3, 4, 5]))


