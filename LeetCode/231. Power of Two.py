class Solution(object):
    def isPowerOfTwo(self, n):
        while n>0:
            if n==1:
                return True
            if n%2!=0:
                return False
            n//=2
        return False
a = Solution()
print(a.isPowerOfTwo(3))