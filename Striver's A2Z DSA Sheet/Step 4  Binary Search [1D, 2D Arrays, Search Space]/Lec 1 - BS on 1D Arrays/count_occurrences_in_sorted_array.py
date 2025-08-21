class Solution(object):
    def bs(self,nums,target,findFirst):
        start,end =0,len(nums)-1
        ans = -1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]==target:
                ans = mid
                if findFirst:
                    end = mid-1
                else:
                    start = mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                start = mid+1
        return ans
    def countOccurrences(self,nums,target):
        first = self.bs(nums,target,True)
        if first==-1:
            return 0
        last = self.bs(nums,target,False)
        occurrences = last-first+1
        return occurrences

a = Solution()
print(a.countOccurrences([1,2,2,2,2,3,4,5,6,6,6,7,8,9],10))