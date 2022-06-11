class Solution:
    def validPalindromic(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        begin, maxlen = 0, 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                x = self.validPalindromic(s, i, j)
                if j + 1 - i > maxlen and x:
                    maxlen = j + 1 - i
                    begin = i
        return s[begin:maxlen]


class SolutionExpandFromCenter:
    # 中心扩散法
    def expandFromCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        n = len(s)
        for i in range(n):
            left1, right1 = self.expandFromCenter(s, i, i)
            left2, right2 = self.expandFromCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


class SolutionDP:
    def longestpalindrome(self, s):
        n = len(s)

        dp = [[False] * n for i in range(n)]

        res = ""

        for length in range(n):
            for i in range(n):
                j = i + length
                if j >= n:
                    break
                if length == 0:
                    dp[i][j] = True
                elif length == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and j + 1 > len(res):
                    res = s[i:j + 1]
        return res


if __name__ == '__main__':
    s = "abcbade"
    x = SolutionDP()
    res = x.longestpalindrome(s)
    print(res)
