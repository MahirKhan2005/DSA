class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num!=val:
                nums[i]=num
                i+=1
                
        return i

a = Solution()
print(a.removeElement([0,1,2,2,3,0,4,2],2))