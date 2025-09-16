class Solution:
    def findDuplicates(self, arr):
        # code here
        s=set()
        d=[]
        for i in arr:
            if i in s:
                d.append(i)
            else:
                s.add(i)
        return d
            
        