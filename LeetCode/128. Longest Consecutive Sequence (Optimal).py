class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num-1 not in num_set:
                length = 1
                while num+length in num_set:
                    length+=1
            if length> max_length:
                max_length = length
        return max_length


a = Solution()
print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))