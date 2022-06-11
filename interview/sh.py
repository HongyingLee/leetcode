# 冒泡排序
import collections

def bubble(nums):
    n = len(nums)
    if n <= 1:
        return nums
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

# 文件中英文单词，统计单词出现的次数 空格/标点符号


def cipin(file):
    with open(file,"rb+") as f:
        data = f.read().split(" ")
        dict_res = {}
        n = len(data)
        for i in range(n):
            if data[i] not in dict_res:
                dict_res[data[i]] = 1
            else:
                dict_res[data[i]] += 1

        # 出现次数排前5的字母及出现的次数
        res = []
        for key,value in dict_res.items():
            res.append(value)

        sorted(res, reverse=True)
        x = res[0:5]
        r = {}
        for i in range(len(x)):
            for key,value in dict_res.items():
                if value == x[i]:
                    r[key] = x[i]
    # return dict_res
    return r

def cipinNew(nums,k):
    res = collections.Counter(nums)
    # most_common(k),前k个最多出现的元素及出现的次数；0：元素值；1： 元素出现的次数
    print(res)
    return [item for item in res.most_common(k)]


if __name__ == '__main__':
    # print(bubble([]))
    # print(bubble([1]))
    # print(bubble([1, 2]))
    # print(bubble([10000000, 0, 1, 700000, 9, 10000000000]))
    # print(bubble([10000000, 0, 1, 1, 700000, 9, 10000000000]))
    # print(bubble([10000000, 1, 5, -1, 700000, 9, 10000000000]))
    print(cipinNew([1,2,3,2,4,5,5,6,5],2))
    nums = [1, 2, 3, 4, 2, 4, 5, 5, 4]
    x = collections.Counter(nums)
    print(x)

    print(sorted(x.elements(),reverse=True))