class Solution(object):
    def nthRoot(self,n,m):
        if m<2:
            return m
        
        start = 1
        end = m
        while start<=end:
            mid = start + (end-start)//2
            root = mid**n
            if root==m:
                return mid
            elif root<m:
                start = mid+1
            else:
                end = mid-1
        return -1

a = Solution()
print(a.nthRoot(3,27))
            