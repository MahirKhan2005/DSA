class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth = depth = 0
        for i in range(len(s)):
            if s[i]=="(":
                depth+=1
            elif s[i]==")":
                depth-=1
            if depth>maxdepth:    
                maxdepth = depth 
        return maxdepth
        