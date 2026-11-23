class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        count=0
        d1=0
        d2=0
        n=len(mat)
        D1=[]
        D2=[]
        
        if n%2==0:
            for i in range(n):
                d1+=mat[i][i]
            for j in range(n):
               k=(j*(-1))-1
               d2+=mat[j][k]
            return d1+d2
           
        if n%2!=0:
            h=n//2
            for i in range(n):
                d1+=mat[i][i]
            for j in range(n):
               k=(j*(-1))-1
               d2+=mat[j][k]
            return d1+d2-mat[h][h]
