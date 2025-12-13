class Solution:
    def swapDiagonal(self, mat):
      # code here
      for i in range(len(mat)):
          mat[i][i],mat[i][n-i-1]=mat[i][n-i-1],mat[i][i]
      return mat
              
