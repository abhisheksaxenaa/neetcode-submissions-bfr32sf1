class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        lIndex = 0
        rIndex = 0
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > (rIndex - lIndex + 1):
                    rIndex = r
                    lIndex = l
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > (rIndex - lIndex + 1):
                    rIndex = r
                    lIndex = l
                l -= 1
                r += 1
        return s[lIndex:rIndex+1]
