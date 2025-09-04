from math import ceil

class Solution(object):
    def eatingTime(self,piles,k):
        time = 0
        for i in range(0,len(piles)):
            time+=ceil(piles[i]/k)
        return time

    def minEatingSpeed(self, piles, h):
        start,end = 1,max(piles)
        while start<end:
            mid = start + (end-start)//2
            totalTime = self.eatingTime(piles,mid)
            if totalTime<=h:
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans

a = Solution()
print(a.minEatingSpeed([3,6,7,11],8))