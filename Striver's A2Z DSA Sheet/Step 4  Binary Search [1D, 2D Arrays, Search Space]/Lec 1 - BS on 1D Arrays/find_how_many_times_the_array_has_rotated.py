class Solution(object):
    def findRotationCount(self,nums):
        start = 0
        end = len(nums)-1
        while start<end:
            mid = start + (end-start)//2
            if nums[mid]>nums[end]:
                start = mid+1
            else:
                end = mid
        return start
    
a = Solution()
print(a.findRotationCount([3,4,5,1,2]))