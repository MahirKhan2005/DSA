class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        start,end = 0,len(arr)-1
        while start<=end:
            mid = start + (end-start)//2
            missing = arr[mid] - (mid+1)
            if missing < k:
                start = mid+1
            else:
                end = mid-1
        return start+k
    
