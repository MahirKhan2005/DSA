class Solution:
    def singleNumber(self, nums) -> int:
        temp = 0
        for num in nums:
            temp^=num
        return temp

a = Solution()
print(a.singleNumber([2,2,2,2,1,2,2]))
        