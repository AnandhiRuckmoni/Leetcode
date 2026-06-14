class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx=-1
        i=0
        j=0
        d={}
        while i <= j and j < len(s):
            windowsize=j-i+1
            if s[j] not in d.keys():
                d[s[j]]=1
            else:
                d[s[j]]+=1
            maxoccurence=sorted(d.items(), key=lambda x:-x[1])[0][1]
            if windowsize-maxoccurence<=k:
                j+=1
            else:
                mx=max(mx,j-i)
                while  windowsize-maxoccurence>k:
                    if s[i] in d.keys():
                        d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1
                    windowsize=j-i+1                                        
                    maxoccurence=sorted(d.items(),key=lambda x:-x[1])[0][1]
                j+=1
        mx=max(mx,j-i)
        return(mx)