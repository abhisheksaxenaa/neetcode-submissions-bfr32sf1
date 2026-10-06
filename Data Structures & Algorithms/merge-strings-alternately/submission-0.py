class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        i = 0
        n = min(len(word1), len(word2))
        while i < n:
            result += word1[i]
            result += word2[i]
            i += 1
        result += word1[i:]
        result += word2[i:]
        return result