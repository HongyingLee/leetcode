def longestSubStr(s):
    occ = set()
    n = len(s)

    result = ""

    rk, res = -1, 0

    for i in range(n):
        if i != 0:
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            occ.add(s[rk + 1])
            rk += 1
        res = max(res, rk + 1 - i)
        if res > len(result):
            result = s[i:i + rk]
    return result


print(longestSubStr("abbcdea"))