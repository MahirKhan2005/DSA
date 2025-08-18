class Solution(object):
    def isPowerOfThree(self, n):
        while n>0:
            if n==1:
                return True
            if n%3!=0:
                return False
            n//=3
        return False