class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                return mid
            # Check which part is sorted
            # If left sorted
            if nums[start]<=nums[mid]:
                if target<=nums[mid] and target>=nums[start]:
                    end = mid-1
                else:
                    start = mid+1
            # If right sorted
            else:
                if target<=nums[end] and target>nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1
a= Solution()
print(a.search([4,5,6,7,0,1,2],9))