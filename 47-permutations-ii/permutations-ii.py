class Solution:
    def permutations(self,l):
        if len(l)==0:
            return [[]]
        firstel=l[0]
        l1=self.permutations(l[1:])
        #print('l1',l1)
        l2=[]
        x=[]
        for i in l1:
            for j in range(len(i)+1):
                #print(i,i[0:j],j,firstel)
                #x=[i[0:j]+firstel+i[j:]]
                x=i[0:j]+[firstel]+i[j:]
                #i.insert(j,firstel)
                if x not in l2:
                    l2.append(x)
        #print(l2)
        return l2
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=self.permutations(nums)
        return ans