# Hashing Approach -> O(n) O(n) - SC due to dictionary
class Solution(object):
    def singleNumber(self, nums):
        hash = {}
        for i in nums:
            hash[i] = hash.get(i,0) + 1
        for i in hash.keys():
            if hash[i]==1:
                return i

# XOR Approach -> O(n) O(1) 
#               a^a = 0, a^0 = a, XORing all will cancel out pairs leaving the answer
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^= i
        return result


a = Solution()
print(a.singleNumber([4,1,2,1,2]))
        