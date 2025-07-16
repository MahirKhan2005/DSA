class Solution(object):
    def bs(self,array,target,start,end):
        if start<=end:
            mid = start + (end-start)//2
            if array[mid] == target:
                return mid
            elif array[mid] <= target:
                return self.bs(array,target,mid+1,end)
            else:
                return self.bs(array,target,start,mid-1)
        return -1
    def search(self, array, target):
        return self.bs(array,target,0,len(array)-1)
    
