class Solution:
    def findDisappearedNumbers(self, nums):
        hash = [0]*(len(nums)+1)
        hash[0] = 1
        ans = []
        for i in nums:
            hash[i] = 1
        for i in range(0,len(hash)):
            if hash[i]==0:
                ans.append(i)
        return ans