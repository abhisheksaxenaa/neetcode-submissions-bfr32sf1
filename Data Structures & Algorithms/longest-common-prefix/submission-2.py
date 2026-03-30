class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        if len(strs) == 1:
            return strs[0]
        if '' in strs:
            return ''
        else:
            pre = shortest[0]
        print(shortest)
        for i in range(len(shortest)):
            for word in strs:
                print(word[0:i+1])
                print(pre)
                if word[0:i+1] != pre:
                    if pre == '':
                        return ''
                    else:
                        return pre[0:i]
                    break
            i = i+1
            pre = word[0:i+1]
        if pre == shortest:
            return pre
        else:
            return pre[:-1]