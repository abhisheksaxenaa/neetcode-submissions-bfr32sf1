class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alp = [0] * 26
        N = len(words)
        for i in range(26):
            alp[ord(order[i]) - ord('a')] = i + 1

        # print(alp)
        for i in range(1, N):
            before = words[i - 1]
            current = words[i]
            j = 0
            while j < len(before):
                if j == len(current):
                    return False
                if alp[ord(before[j]) - ord('a')] < alp[ord(current[j]) - ord('a')]:
                    break
                elif alp[ord(before[j]) - ord('a')] > alp[ord(current[j]) - ord('a')]:
                    return False
                j += 1
            # if len(current) == j:
        return True
