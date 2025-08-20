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
    
# Two pointer approach - O(n) O(1) only for positives
class Solution():
    def findSubarrayLength(self,nums,k):
        left = 0
        curr_sum = 0
        max_sum = 0
        for right in range(0,len(nums)):
            curr_sum+=nums[right]

            while curr_sum>k and left<=right:
                curr_sum-=nums[left]
                left+=1

            if curr_sum==k and curr_sum>max_sum:
                max_sum = curr_sum
        return max_sum
    
# Hashing + Prefix Sum - 
class Solution():
    def findSubarrayLength(self,nums,k):
        hash = {}
        prefixSum = 0
        max_len = 0
        for i in range(0,len(nums)):
            prefixSum+=nums[i]
            
            if prefixSum==k:
                max_len = max(max_len,i+1)

            if (prefixSum-k) in hash:
                curr_len = i - hash[prefixSum-k]
                max_len = max(curr_len,max_len)
            
            if prefixSum not in hash:
                hash[prefixSum] =  i
        return max_len

a = Solution()
print(a.findSubarrayLength([1,2,1,1,1,3,2],5))
