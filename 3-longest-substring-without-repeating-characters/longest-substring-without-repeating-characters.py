class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        s1=""
        mx=0
        while j < len(s):
            if s[j] not in s1:
                s1+=s[j]
            else:
                while s[j] in s1:
                    mx=max(mx,len(s1))
                    s2=s1[1:]
                    s1=s2
                    i+=1
                s1+=s[j]
            j+=1
            #print(s1,mx,i,j)
        mx=max(mx,len(s1))
        return mx