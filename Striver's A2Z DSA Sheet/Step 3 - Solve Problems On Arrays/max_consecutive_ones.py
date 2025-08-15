class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_ones = 0
        max_ones = 0
        for i in range(0,len(nums)):
            if nums[i]==1:
                current_ones+=1
            if current_ones>max_ones:
                max_ones = current_ones
            elif nums[i]!=1:
                current_ones = 0
        return max_ones
a = Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1,0,0,0,1,1,1,1,0]))