# Brute force - O(n^2)
class Solution(object):
    def moveZeroes(self, nums):
        for i in range(-1,-len(nums)-1,-1):
            if nums[i]==0:
                temp = nums.pop(i)
                nums.append(temp)
        return nums        

# Two pointer approach - O(n)
class Solution(object):
    def moveZeroes(self, nums):
        pos = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0
        return nums

a = Solution()
print(a.moveZeroes([0,0,1]))