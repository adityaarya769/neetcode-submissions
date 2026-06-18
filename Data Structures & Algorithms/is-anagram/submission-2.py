class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 1
            else:
                dct[s[i]] += 1
            
            if t[i] not in dct:
                dct[t[i]] = -1
            else:
                dct[t[i]] += -1

        for i in dct:
            if dct[i] != 0:
                return False
        return True




