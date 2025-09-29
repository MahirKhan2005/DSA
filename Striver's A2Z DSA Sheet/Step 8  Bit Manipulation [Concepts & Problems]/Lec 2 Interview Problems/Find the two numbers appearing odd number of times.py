class Solution:
    def singleNumber(self, nums):
        xorAll = 0
        for num in nums:
            xorAll^=num
        setBit = xorAll & ~(xorAll-1)
        num1,num2 = 0,0
        for num in nums:
            if num & setBit:
                num1^=num
            else:
                num2^=num
        return [num1,num2]