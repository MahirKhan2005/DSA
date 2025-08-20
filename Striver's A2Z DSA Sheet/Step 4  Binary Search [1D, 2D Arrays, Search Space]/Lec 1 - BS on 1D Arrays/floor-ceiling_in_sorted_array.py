class Solution(object):
    def floor(self,nums,k):
        start = 0
        end = len(nums)-1
        ans  = None
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==k:
                return nums[mid]
            elif nums[mid]<k:
                ans = nums[mid]
                start = mid+1
            else:
                end = mid-1
        return ans
    def ceil(self,nums,k):
        start = 0
        end = len(nums)-1
        ans = None
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]==k:
                return nums[mid]
            elif nums[mid]>k:
                ans = nums[mid]
                end = mid-1
            else:
                start = mid+1
        return ans



a=Solution()
print(a.floor([3, 4, 4, 7, 8, 10],5))
print(a.ceil([3, 4, 4, 7, 8, 10],5))
