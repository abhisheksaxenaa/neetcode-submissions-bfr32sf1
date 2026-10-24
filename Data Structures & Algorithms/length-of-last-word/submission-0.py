class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while s[i] == ' ' and i >= 0:
            i -= 1
        j = i
        while s[j] != ' ' and j >= 0:
            j -= 1
        return i - j