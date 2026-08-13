class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        total = len(t)
        window = {}
        window_count = 0
        result = (0,0)
        min_len = float("infinity")

        for i in range(total):
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
        
        l = 0
        for r in range(len(s)):
            # if s[r] not in t_count:
            #     continue
            c = s[r]

            window[c] = 1 + window.get(c, 0)
            if c in t_count and window[c] <= t_count[c]:
                window_count += 1
            while window_count == total:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    result = (l, r)
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    window_count -= 1
                l += 1
        (l, r) = result
        return s[l : r + 1] if min_len != float("infinity") else ""
        
# OUZOYDYXAZV
