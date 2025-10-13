class Solution:
    def binaryGap(self, n: int) -> int:
        dist = 0
        maxDist = 0
        count = 0
        while not n&1:
            n>>=1
        while n>0:
            if n&1:
                dist = 0
            else:
                dist+=1
            maxDist = max(dist,maxDist)
            count+=n&1
            n>>=1
        if count<2:
            return 0
        return maxDist+1