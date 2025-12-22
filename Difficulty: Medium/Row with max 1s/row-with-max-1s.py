class Solution:
    def rowWithMax1s(self, arr):
        # code here
        m=0
        s=0
        ans=-1
        for i in range(len(arr)):
            s=sum(arr[i])
            if s>m:
                m=s
                ans=i
        return ans
                
            