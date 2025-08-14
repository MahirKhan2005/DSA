class Solution():
    def search(self,nums,num):
        for i in range(0,len(nums)):
            if nums[i]==num:
                print(f"{num} is present at index {i}")
                return
        print(f"{num} is not present in the array")
        return

a = Solution()
a.search([1,2,3,6,7,9,0],7)