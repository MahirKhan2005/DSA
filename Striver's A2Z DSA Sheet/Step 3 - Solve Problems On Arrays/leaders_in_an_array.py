class Solution(object):
    def printLeaders(self,nums):
        max_num = nums[-1]

        # Iteration will start from the last second element
        i = len(nums)-2

        # Creating a list with just the last element fo nums
        ans = [max_num]

        while i>=0:
            if nums[i]>max_num:
                ans.append(nums[i])
                max_num = nums[i]
            i-=1
        return ans 
    
a = Solution()
print(a.printLeaders( [10, 22, 12, 3, 0, 6]))
            