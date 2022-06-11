def find_left(s, i):
    res = s[i]
    j = i - 1
    while j >= 0:
        if s[j] not in res:
            res += s[j]
        j -= 1
    return len(res)


def findLongStr(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    length = 0
    for i in range(len(s)):
        length = max(length, find_left(s, i))
    return length


if __name__ == '__main__':
    print(findLongStr("abcabcab"))

