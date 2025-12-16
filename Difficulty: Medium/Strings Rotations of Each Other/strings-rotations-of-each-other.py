class Solution:
    def areRotations(self, s1, s2):
        # code here
        r=s1+s1
        if s2 in r:
            return True
        else:
            return False
        