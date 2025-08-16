# Hashing - O(n) O(n)
class Solution(object):
    def majorityElement(self,nums):
        map = {}
        for num in nums:
            map[num] = map.get(num,0) + 1
        for i in map.keys():
            if map[i] > len(nums)/2:
                return i

# Boyer Moore's Voting Algorithm - O(n) O(1) 
# Slower in python, fast in C++
class Solution(object):
    def majorityElement(self,nums):
        candidate = None
        count = 0
        for i in range(0,len(nums)):
            if count==0:
                candidate = nums[i]
            count+=(1 if candidate==nums[i] else -1)
        return candidate
a = Solution()
print(a.majorityElement([3,2,3]))