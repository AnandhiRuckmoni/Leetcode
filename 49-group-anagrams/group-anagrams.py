class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        l=[]
        l1=[]
        for i in strs:
            val="".join(sorted(i))            
            if val not in d.keys():
                l.append(i)
                d[val]=l
                l=[]
            else:
                d[val].append(i)
        for i in d.values():
            l1.append(i)
        return l1