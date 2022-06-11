#[1,3,2,4,5]
#[(1,4),(2,3)]
def twoSum(nums,target):
    res = []
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = []
            if nums[i] + nums[j] == target:
                s.append(nums[i])
                s.append(nums[j])
                res.append(s)
    return res


if __name__ == '__main__':
    nums = [1,3,2,4,5]
    target = 5
    print(twoSum(nums,target))