class Solution:
    def findComplement(self, num: int) -> int:
        n = num
        i = 0
        while n>0:
            n>>=1
            i<<=1
            i^=1
        return num^i