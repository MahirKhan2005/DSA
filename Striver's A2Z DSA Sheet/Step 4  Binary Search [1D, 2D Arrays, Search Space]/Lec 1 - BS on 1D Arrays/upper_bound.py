class Solution(object):
    def upperBound(self,nums,k):
        ans = len(nums)
        start = 0
        end = len(nums) - 1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]<=k:
                start = mid+1
            else:
                ans = mid
                end = mid-1
        return ans
    

    
a = Solution()
print(a.upperBound([3,5,8,9,15,19],9))