class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        m, n = len(word1), len(word2)
        # not using result = '' and result += word[i]
        # because this will create another string and the
        # TC becomes O(n^2) instead of O(m + n)
        while i < max(m, n):
            if i < m:
                result.append(word1[i])
            if i < n:
                result.append(word2[i])
            i += 1
        return ''.join(result)