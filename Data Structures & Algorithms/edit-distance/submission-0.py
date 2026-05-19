class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        # if word1[i - 1] == word[j - 1] then dp[i][j] = dp[i-1][j-1]
        # else dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j-1])

        # Why i-1 and j-1 while matching word is because
        # the index in dp is 1 greater, so to check the actual position in word
        # we have to sub by 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j-1])
        # print(dp)
        return dp[m][n]
