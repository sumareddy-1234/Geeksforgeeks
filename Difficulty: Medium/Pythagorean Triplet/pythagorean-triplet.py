class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	s=set()
    	for i in arr:
    	    s.add(i*i)
    	
    	n=len(arr)
    	
    	for i in range(n):
    	    for j in range(i+1,n):
    	        if arr[i]*arr[i]+arr[j]*arr[j] in s:
    	            return True
    	return False