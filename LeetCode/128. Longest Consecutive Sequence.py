# TC - O(nlogn)
class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        curr_count = 1
        max_count = 0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                curr_count+=1
                if curr_count>max_count:
                    max_count=curr_count
            elif nums[i]==nums[i-1]:
                continue
            else:
                curr_count = 1
        return max_count
    
a = Solution()
print(a.longestConsecutive([1,2,2,2,2,2,3,4,5,6,7]))