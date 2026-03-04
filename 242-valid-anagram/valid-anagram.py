class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[]
        if len(s)!=len(t):
            return False
        for i in t:
            if i not in l:
                if i not in s:
                    return False
                else:
                    if t.count(i)!=s.count(i):
                        return False
                l.append(i)
        return True