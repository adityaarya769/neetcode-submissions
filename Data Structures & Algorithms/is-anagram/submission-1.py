class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in dct_s:
                dct_s[s[i]] = 1
            else:
                dct_s[s[i]] = dct_s.get(s[i]) + 1
            
            if t[i] not in dct_t:
                dct_t[t[i]] = 1
            else:
                dct_t[t[i]] = dct_t.get(t[i]) + 1
        
        for i in dct_s:
            if dct_s.get(i) != dct_t.get(i):
                return False
        return True



