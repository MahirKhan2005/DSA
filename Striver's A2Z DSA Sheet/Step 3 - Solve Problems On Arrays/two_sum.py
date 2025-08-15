class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in d:
                return [d[compliment],i]
            d[num] = i
a = Solution()      
print(a.twoSum([3,2,4],6))
        