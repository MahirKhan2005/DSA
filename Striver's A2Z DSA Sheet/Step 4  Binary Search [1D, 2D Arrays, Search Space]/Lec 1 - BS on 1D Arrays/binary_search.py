class Solution(object):
    def search(self,nums,target):
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid-1
        return -1
a=Solution()
print(a.search([1,2,3,4,5],4))