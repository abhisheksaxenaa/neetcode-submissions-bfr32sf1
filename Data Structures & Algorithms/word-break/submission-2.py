class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        # Approach : 1
        # def dfs(i):
        #     if i == n:
        #         return True
        #     for word in wordDict:
        #         w = len(word)
        #         if (i + w) <= n and s[i : i + w] == word:
        #             if dfs(i + w):
        #                 return True
        #     return False
        # return dfs(0)
        # n = len(s)

        # Approach 2: using set for wordset, memoization in recursion
        wordDictSet = set(wordDict)
        memo = {0: True}
        def dfs(i):
            if i in memo:
                return memo[i]
            for j in range(i, -1, -1):
                if s[j: i] in wordDictSet:
                    if dfs(j):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(n)
        # Approach 3: using iterative approach
