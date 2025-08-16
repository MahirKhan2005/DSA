# Brute Force Approach - O(n^2) O(1)
class Solution():
    def findSubarrayLength(self,nums,k):
        max_length = 0
        for i in range(0,len(nums)):
            sum = 0
            count = 0
            for j in range(i,len(nums)):
                sum+=nums[j]
                count+=1
                if sum==k and count>max_length:
                    max_length = count
        return max_length
    


a = Solution()
print(a.findSubarrayLength([-1,1,1],1))
