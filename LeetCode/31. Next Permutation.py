class Solution:
    def nextPermutation(self,nums):
        i = len(nums)-1
        if nums==sorted(nums,reverse=True):
            nums.sort()
            return nums
        
        # Finding pivot 
        while i>0:
            if nums[i]>nums[i-1]:
                pivot = i-1
                break 
            i-=1
        
        # Finding the next smallest element
        for j in range(pivot+1,len(nums)):
            if nums[j]>nums[pivot]:
                nex_elem = j
        
        # Swapping the next samllest with pivot
        nums[pivot],nums[nex_elem] = nums[nex_elem],nums[pivot] 


        # Reversing the subarray 
        i,j = pivot+1,len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums
    

a = Solution()
print(a.nextPermutation([1,5,4,3,2]))
        