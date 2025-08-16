# Brute Forse Approach - Time limit exceeded - O(n^2) O(1)
class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max_sum = nums[0]
        for i in range(0,len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum>max_sum:
                    max_sum = sum
        return max_sum

# Kadane's Algorithm - O(n) O(1)
#   - says that if we the sum becomes <0 then reset it to zero(discard the previous subarray as its sum is contributing negatively)
class Solution(object):
    def maxSubArray(self, nums):
        sum = nums[0]
        curr_sum = 0
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            sum = max(curr_sum,sum)
            if curr_sum<0:
                curr_sum = 0
        return sum


a = Solution()
print(a.maxSubArray([-1]))