class Solution:
    def subseq(self,txt,pat,i,j,n,m,dp):
        if j == m:
            return 1
        if i==n and j < m:
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]
        if txt[i]!=pat[j]:
            return self.subseq(txt,pat,i+1,j,n,m,dp)
        else:
            dp[i][j]= self.subseq(txt,pat,i+1,j+1,n,m,dp) + self.subseq(txt,pat,i+1,j,n,m,dp)
            return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        
        dp=[[-1 for i in range(len(t))] for j in range(len(s))]
        return self.subseq(s,t,0,0,len(s),len(t),dp)
        