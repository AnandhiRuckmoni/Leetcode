class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in range(len(s)):
            if s[i] not in d.keys():
                if t[i] not in d.values():
                    d[s[i]]=t[i]
                else:
                    return False
            else:
                if d[s[i]]!=t[i]:
                    return False
        return True