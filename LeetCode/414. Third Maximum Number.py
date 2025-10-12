class Solution:
    def thirdMax(self, nums) -> int:
        nums.sort()
        maximum = nums[-1]
        flag = False
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<maximum:
                secondMax = nums[i]
                flag = True
                break
        if flag:
            for i in range(len(nums)-1,-1,-1):
                if nums[i]<secondMax:
                    return nums[i]
        return maximum