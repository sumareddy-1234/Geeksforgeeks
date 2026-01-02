class Solution:
    def sort012(self, arr):
        # code here
        z=[]
        o=[]
        t=[]
        for i in arr:
            if i==0:
                z.append(i)
            elif i==1:
                o.append(i)
            else:
                t.append(i)
        arr[:]=z+o+t