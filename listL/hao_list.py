# [1,1,1,3,3,4,1]
# res:[[1,1,1],[3,3][4],[1]]

def sortList(nums):
    n = len(nums)
    resAll = []
    res = []
    if len(nums) == 0:
        return []
    flag = nums[0]
    for i in range(n):
        if nums[i] == flag:
            res.append(nums[i])
        else:
            resAll.append(res)
            flag = nums[i]
            res = []
            res.append(nums[i])
    resAll.append(res)
    return resAll


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 1]
    print(sortList(nums))
