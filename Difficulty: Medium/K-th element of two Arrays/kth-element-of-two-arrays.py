class Solution:
    def kthElement(self, a, b, k):
        # code here
        l=a+b
        l.sort()
        return l[k-1]
        