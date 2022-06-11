#1、	给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1
# 如：字符串“titok” 返回 1

def findFirstChar(s):
    hashTable = {}
    # key:i
    # value:i出现的次数
    for i in s:
        if i not in hashTable:
            hashTable[i] = 1
        else:
            hashTable[i] += 1

    res = []

    for key,value in hashTable.items():
        if value == 1:
            res.append(s.index(key))

    if not res:
        return -1
    else:
        return min(res)


if __name__ == '__main__':
    print(findFirstChar("aabbcc"))