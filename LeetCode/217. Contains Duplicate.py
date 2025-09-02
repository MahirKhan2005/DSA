class Solution(object):
    def containsDuplicate(self, nums):
        hash = {}
        for num in nums:
            hash[num] = hash.get(num,0) + 1
        for i in hash:
            if hash[i]>1:
                return True
        return False

