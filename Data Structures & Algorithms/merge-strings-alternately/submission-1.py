class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        m, n = len(word1), len(word2)
        while i < max(m, n):
            if i < m:
                result.append(word1[i])
            if i < n:
                result.append(word2[i])
            i += 1
        # result += word1[i:]
        # result += word2[i:]
        return ''.join(result)