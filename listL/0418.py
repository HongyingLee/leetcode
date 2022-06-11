def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    nums1[m:m+n] = nums2
    length = len(nums1)
    for i in range(length - 1):
        if nums1[i] > nums1[i + 1]:
            nums1[i + 1] = nums1[i]
    return nums1


if __name__ == "__main__":
    print(merge([1,2,3],[3,4]))
