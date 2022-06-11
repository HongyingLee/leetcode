# 有一个字符串，小写字母，找出出现频率最高的字符，以及首次出现的索引，有多个出现频次相同的字符，只返回首先达到最高频次的字符以及下标值


def findChar(s):
    hashTalbe = {}
    hashTalbe_index = {}
    n = len(s)

    for i in range(n):
        if s[i] not in hashTalbe:
            hashTalbe[s[i]] = 1
        else:
            hashTalbe[s[i]] += 1

        if s[i] not in hashTalbe_index:
            hashTalbe_index[s[i]] = i

    res = ""
    res_index = -1

    x = max(hashTalbe.values())
    print(x)
    print(hashTalbe)
    print(hashTalbe_index)
    for key, value in hashTalbe.items():
        # print(key,value)
        if hashTalbe[key] == x:
            res = key
            break

    for key, value in hashTalbe_index.items():
        # print(key,value)
        if key == res:
            res_index = hashTalbe_index[key]

    return res, res_index


if __name__ == '__main__':
    s = "abcab"
    print(findChar(s))
