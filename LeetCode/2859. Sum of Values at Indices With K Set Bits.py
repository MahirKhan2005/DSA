class Solution:
    def sumIndicesWithKSetBits(self, nums, k: int) -> int:
        total = 0
        for i in range(len(nums)):
            count = 0
            index = i
            while i>0:
                i&=i-1
                count+=1
            if count==k:
                total+=nums[index]
        return total