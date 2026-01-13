class Solution:
    def canServe(self, arr):
        # code here 
        f,ten=0,0
        for i in arr:
            if i==5:
                f+=1
            elif i==10:
                ten+=1
                if f>=1:
                    f-=1
                else:
                    return False
            elif i==20:
                if ten>=1 and f>=1:
                    f-=1
                    ten-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True
        