class Solution:
    def checkPalindrome(self, s: str, i: int, j: int, flag: bool) -> bool:
        if i > j:
            return True
        if s[i] == s[j]:
            return self.checkPalindrome(s, i + 1, j - 1, flag)
        if not flag:
            return False
        return self.checkPalindrome(s, i + 1, j, False) or self.checkPalindrome(s, i, j - 1, False)
    def validPalindrome(self, s: str) -> bool:
        # count = 1
        i, j = 0, len(s) - 1
        # print(i, ':', j, s[i:j+1])
        # while i <= j:
        #     if s[i] == s[j]:
        #         i += 1
        #         j -= 1
        #     elif count:
        #         print(i, ':', j, s[i:j+1])
        #         if s[i + 1] == s[j]:
        #             i += 1
        #         else:
        #             j -= 1
        #         count = 0
        #     else:
        #         print(i, ':', j, s[i:j+1])
        #         return False
        # return True
        return self.checkPalindrome(s, i, j, True)