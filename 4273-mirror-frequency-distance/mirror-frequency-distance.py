class Solution:
    def mirrorFrequency(self, s: str) -> int:
        l=[]
        visited=[]
        for i in s:
            if i not in visited:
                if i.isnumeric():
                    dist=int(i)
                    distmirror=9-dist
                    l.append(abs(s.count(i)-s.count(str(distmirror))))
                    visited.append(i)
                    if s.count(str(distmirror))!=0:
                        visited.append(str(distmirror))
                else:
                    dist=ord(i)-97
                    distmirror=ord('z')-dist
                    l.append(abs(s.count(i)-s.count(chr(distmirror))))
                    if s.count(chr(distmirror))!=0:
                        visited.append(chr(distmirror))
                    visited.append(i)
                
        return(sum(l))