class Solution:
    def missingRange(self, arr, low, high):
        #code here
        arr=set(arr)
        res=[]
        for i in range(low,high+1):
            if i not in arr:
                res.append(i)
        return res