class Solution:    
    def findUnion(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        res=a|b
        return res