class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        d1={}
        d2={}
        n=len(s1)
        for i in range(n):
            if s1[i] in d1 or s2[i] in d2:
                if d1.get(s1[i])!=s2[i] or d2.get(s2[i])!=s1[i]:
                    return False
            
            d1[s1[i]]=s2[i]
            d2[s2[i]]=s1[i]
        return True