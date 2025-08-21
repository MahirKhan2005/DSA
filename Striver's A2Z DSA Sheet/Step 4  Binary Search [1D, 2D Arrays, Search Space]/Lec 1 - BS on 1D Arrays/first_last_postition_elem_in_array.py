class Solution(object):
    def bs(self, nums, target,findFirst):
        start = 0
        end = len(nums)-1
        ans = -1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                ans =  mid
                if findFirst:
                    end = mid-1
                else: 
                    start = mid+1
            elif nums[mid]<target:
                start = mid+1
            else:
                end = mid-1
        return ans
    def searchRange(self, nums, target):
        first = self.bs(nums,target,True)
        last = self.bs(nums,target,False)
        return [first,last]
a = Solution()
print(a.searchRange([],0))