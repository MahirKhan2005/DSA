class Solution(object):
    def isPowerOfFour(self, n):
        while n>0:
            if n==1:
                return True
            if n%4!=0:
                return False
            n//=4
        return False