from bisect import bisect_left,bisect_right
class Solution:
    def cntInRange(self, arr, queries):
        # code here
        arr.sort()
        res=[]
        for a,b in queries:
            c=0
            start=bisect_left(arr,a)
            end=bisect_right(arr,b)
            c=end-start
            res.append(c)
                    
        return res
            
                
                
        