class Solution(object):
    def lowerBound(self,nums,target):
        start = 0
        end = len(nums)-1
        ans = len(nums)
        while start<=end:
            mid = start + (end-start)//2 
            if nums[mid]>=target:
                ans = mid
                end = mid-1
            else:
                start = mid+1
        return ans

a = Solution()
print(a.lowerBound([1,2,3,4,5],2))