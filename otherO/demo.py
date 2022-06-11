def score_cal(t):
    with open(t) as f:
        data = f.read()
        print(data.replace(" ", ","))
        print(type(data))


if __name__ == '__main__':
    score_cal("/Users/hannah/Documents/Python/leetcode/score.txt")
