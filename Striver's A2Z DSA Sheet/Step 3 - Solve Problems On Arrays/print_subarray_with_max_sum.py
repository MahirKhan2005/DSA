class Solution(object):
    def maxSubarray(self,nums):
        curr_sum = 0
        max_sum = nums[0]
        start = 0
        end = 0
        temp_start = 0
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            if curr_sum>max_sum:
                max_sum = curr_sum
                start = temp_start
                end = i
            if curr_sum<0:
                curr_sum=0
                temp_start=i+1

        return nums[start:end+1]
    
a = Solution()
print(a.maxSubarray([-2,1,-3,4,-1,2,1,-5,4] ))

