class Solution:
    def sortIt(self, arr):
        # code here
        odd=[]
        even=[]
        for i in arr:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        odd.sort(reverse=True)
        even.sort()
        arr[:]=odd+even
        
    
