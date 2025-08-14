class Solution(object):
    def sortColors(self, nums):
        count_0 = 0
        count_1 = 0
        count_2 = 0
        # Full iteration, counting the number of 0s, 1s and 2s
        for i in range(0,len(nums)):
            if nums[i]==0:
                count_0+=1
            elif nums[i]==1:
                count_1+=1
            else:
                count_2+=1
        # Mutating value for zero
        for i in range(0,count_0):
            nums[i]=0
        # Mutating value for one
        for i in range(count_0,count_0+count_1):
            nums[i]=1
        # Mutating value for two
        for i in range(count_0+count_1,len(nums)):
            nums[i]=2
        return nums
    
a = Solution()
print(a.sortColors([2,0,2,1,1,0]))