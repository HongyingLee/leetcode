def countS(s):
    hashTable = {}
    n = len(s)
    for i in range(n):
        if s[i] not in hashTable:
            hashTable[s[i]] = 1
        else:
            hashTable[s[i]] += 1
    return hashTable

# 字符串取最长不重复子串
def longestSubstring(s):
    occ = set()
    rk,ans = -1, 0
    n = len(s)
    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            occ.add(s[rk + 1])
            rk += 1
        ans = max(ans, rk - i + 1)
    return s[rk - i:ans]

# ""
# a
# abcabcd：取字符串前半截/中间
# 两个长度相等的不重复子串：abcdabce：qqqq
# 非字符串类型：整数、小数、列表、字典
# 字母+阿拉伯数字+中文+特殊符号（@#￥%……     ）
# 超长字符串：200：199、200、201 100000
# 大小写区分



if __name__ == '__main__':
    s = "abcadb"
    # print(countS(s))
    print(longestSubstring(s))
