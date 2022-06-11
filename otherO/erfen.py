def erfen(nums,target):
    n = len(nums)
    l = 0
    r = n -1
    if n == 0:
        return -1
    while l <= r:
        mid = int(l + (r - l) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid -1
    return -1