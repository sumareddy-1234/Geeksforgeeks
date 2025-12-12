class Solution:
    def transpose(self, mat):
        # code here
        row=len(mat)
        col=len(mat[0])
        res=[]
        for i in range(row):
            res.append([0]*col)
        for j in range(row):
            for k in range(col):
                res[k][j]=mat[j][k]
        return res
            
            