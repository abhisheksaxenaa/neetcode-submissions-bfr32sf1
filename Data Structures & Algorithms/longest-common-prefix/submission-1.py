class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        match = list(strs[0])
        i = len(match)
        for ch in strs:
            j = 0
            for c in range(len(ch)):
                if c < i and ch[c] == match[c]:
                    j = max(j, c + 1)
                else:
                    break
            i = min(i, j)
        return "".join(match)[0:i]