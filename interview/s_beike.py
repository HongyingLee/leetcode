from collections import Counter
# 字符串中出现次数最多的元素

def s_beike(s):
    hashtable = {}
    for i in range(len(s)):
        if s[i] not in hashtable:
            hashtable[s[i]] = 1
        else:
            hashtable[s[i]] += 1
    res = max(hashtable.values())
    for key,value in hashtable.items():
        if value == res:
            return key
# 统计词频
def s_beike_2(s):
    hashtable = Counter(s)
    print(hashtable)
    return hashtable.most_common(1)[0][0]


if __name__ == '__main__':
    s = "abcdddda"
    print(s_beike(s))
    print(s_beike_2(s))
