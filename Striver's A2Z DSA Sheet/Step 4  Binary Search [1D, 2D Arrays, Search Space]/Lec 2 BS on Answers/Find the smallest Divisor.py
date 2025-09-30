import math as m 
class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        start = 1
        end = max(nums)
        while start<end:
            mid = start + (end-start)//2
            sumDiv = 0
            # Sum of the divisions
            for num in nums:
                sumDiv+=m.ceil(num/mid)
            if sumDiv>threshold:
                start = mid+1
            else:
                end = mid
        return start

a = Solution()
print(a.smallestDivisor([1,2,5,9],6))