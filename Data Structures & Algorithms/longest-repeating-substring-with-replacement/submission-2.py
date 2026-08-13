class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        l = 0
        max_count = 0
        res = 0
        n = len(s)
        for r in range(n):
            count[ord(s[r]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[r]) - ord('A')])

            while (r - l + 1) - max_count > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
