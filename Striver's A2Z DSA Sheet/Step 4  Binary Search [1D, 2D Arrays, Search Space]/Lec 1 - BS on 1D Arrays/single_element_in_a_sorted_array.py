class Solution(object):
    def singleNonDuplicate(self, nums):
        start = 1
        end = len(nums)-2
        
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        elif nums[-1]!=nums[-2]:
            return nums[-1]
        
        while start<end:
            mid = start + (end-start)//2
            if (nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            if (mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2==1 and nums[mid]==nums[mid+1]):
                end = mid-1
            else:
                    start = mid+1
        return nums[start]
    
a = Solution()
print(a.singleNonDuplicate([1,1,2,2,3,4,4]))
        

            