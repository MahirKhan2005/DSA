class Solution(object):
        
    def stringIsPalindrome(self,s):
        if len(s)<=1:
            return True
        if s[0]!=s[-1]:
            return False
        return self.stringIsPalindrome(s[1:-1])
    

    
    
