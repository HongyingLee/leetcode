# 统计词频

def countNum(file):
    hashTable = {}
    with open(file) as f:
        data = f.read()
        nums = data.split(",")
        length = len(nums)
        for i in range(length):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = 1
            else:
                hashTable[nums[i]] += 1

    n = len(hashTable)
    if n <= 3:
        return hashTable

    return hashTable

"""
大数量倒序查询5条数据；
requests
file：header需要怎么填写；
发测试报告的框架--allureport
pytest--learn
logging
pymql
linux？

自动化测试平台开发能力
falsk

case分层

刷leetcode：



"""