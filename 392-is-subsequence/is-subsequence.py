import sys
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        cnt=0
        while i<len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
                j+=1
                cnt+=1
            else:
                j+=1
        if i < len(s):
            return False
        else:
            if cnt==len(s):
                return True
            else:
                return False
