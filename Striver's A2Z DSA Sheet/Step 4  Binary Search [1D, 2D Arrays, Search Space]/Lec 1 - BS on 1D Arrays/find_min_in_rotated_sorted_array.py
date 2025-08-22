class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums)-1
        minimum = nums[0]
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]<minimum:
                minimum = nums[mid]
            if nums[start]<=nums[mid]:
                curr_min = nums[start]
                if curr_min<minimum:
                    minimum = curr_min
                start = mid+1
            else: 
                curr_min = nums[end]
                if curr_min<minimum:
                    minimum = curr_min
                end = mid-1
        return minimum
a= Solution()
print(a.findMin([2,3,4,5,1]))

