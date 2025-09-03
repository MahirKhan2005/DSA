class Solution(object):
    def sqrt(self,n):
        if n<2:
            return n
        start = 1
        end = n
        while start<=end:
            mid = start + (end-start)//2
            sqr = mid*mid
            if sqr==n:
                return mid
            elif sqr<n:
                ans = mid
                start = mid+1
            else:
                end = mid-1
        return ans

a = Solution()
print(a.sqrt(139872))
            