class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        res=0
        for i,j in zip(chairs,passengers):
            res+=abs(i-j)
        return res
            
        
