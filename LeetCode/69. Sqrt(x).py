class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        start,end = 1,x
        while start<=end:
            mid = start + (end-start)//2
            sqr = mid*mid
            if sqr==x:
                return mid
            elif sqr<x:
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans
        
a = Solution()
print(a.mySqrt(0))