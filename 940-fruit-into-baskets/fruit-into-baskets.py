class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        j=0
        mx=0
        s=set()
        l=[]
        while j < len(fruits):
            if len(s) < 2:
                if fruits[j] in s:
                    l.append(fruits[j])
                else:
                    s.add(fruits[j])
                    l.append(fruits[j])
                j+=1
            else:
                if fruits[j] in s:
                    l.append(fruits[j])
                    j+=1
                else:
                    mx=max(mx,len(l))
                    lastitem = l[len(l)-1]
                    lastbutoneidx  = len(l)-2
                    while lastbutoneidx >=0 and l[lastbutoneidx]==lastitem:
                        lastbutoneidx-=1
                    if lastbutoneidx >=0:
                        element=l[lastbutoneidx]
                        del l[:lastbutoneidx+1]
                        s.remove(element)
                    if fruits[j] not in s:
                        s.add(fruits[j])
                        l.append(fruits[j])
                    else:
                        l.append(fruits[j])
                    j+=1
        mx=max(mx,len(l))        
        return mx
                