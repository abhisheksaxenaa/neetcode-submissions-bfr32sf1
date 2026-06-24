'''
s1 = abc
s2 = lec abee




0:1,1:1,2:1=> 1,1,1,0000000

11:1,4:1,2:1
0,0,1,0,1,......1,00000000


'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map_s1 = [0 for _ in range(26)] ## choti
        char_map_s2 = [0 for _ in range(26)]

        ls1 = len(s1)
        ls2 = len(s2)
        if ls2 < ls1:
            return False

        # store the characters count in map_s1
        for c in s1:
            char_map_s1[ord(c) - 97] += 1
        
        # store the characters count upto length of s1 in map_s2
        for i in range(ls1):
            char_map_s2[ord(s2[i]) - 97] += 1
            
        

        def isMatching():
            # Check if the two maps are matching or not
            # Should be TC: O(1), SC: O(1)
            for i in range(26):
                if char_map_s1[i] != char_map_s2[i]:
                    return False
            return True

        i = 0
        j = ls1-1

        # i to j works as sliding window
        while j < ls2:
            # Check if maps are matching
            if isMatching():
                return True

            # sliding window of (i,j) by 1
            # if not, then remove i char from map
            # add j + 1 char in map
            # increment i
            char_map_s2[ord(s2[i]) - 97] -= 1
            j += 1
            if j < ls2:
                char_map_s2[ord(s2[j]) - 97] += 1
            i += 1

        return False