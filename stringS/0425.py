def demo(s):
    s_l = s.split(" ")
    res = ""
    for i in range(len(s_l)):
        print(s_l[i])
        r = ""
        j = len(s_l[i])
        while j > 0:
            r += s_l[i][j - 1]
            j -= 1
        res += r
        res += " "
    return res


if __name__ == "__main__":
    print(demo("my name is wangjie"))
