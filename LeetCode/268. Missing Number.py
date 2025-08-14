class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        if nums[0]!=0:
            k=0
        else:
            k = nums[-1]+1
        for i in range(0,len(nums)-1):
            if nums[i+1]-nums[i]!=1:
                k = (nums[i+1]+nums[i])//2
        return k
a = Solution()
print(a.missingNumber([1,2,3]))