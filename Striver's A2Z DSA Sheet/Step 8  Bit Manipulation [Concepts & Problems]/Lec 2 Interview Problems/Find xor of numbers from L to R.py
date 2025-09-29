class Solution:
    def XORTillN(self,n):
        if n%4==1:
            return 1
        if n%4==2:
            return n+1
        if n%4==3:
            return 0
        return n

    def findRangeXOR(self,l,r):
        return self.XORTillN(r)^self.XORTillN(l-1)