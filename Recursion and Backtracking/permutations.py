class Solution(object):
    def permutation(self,nums,permute_set,current):
        if len(current) == len(nums):
            permute_set.append(current[:])
            return
        for i in nums:
            if i in current:
                continue
            current.append(i)
            self.permutation(nums,permute_set,current)
            current.pop()
        return permute_set
    def permute(self,nums):
        return self.permutation(nums,[],[])

num_object = Solution()
print(num_object.permute([1,2,3]))

