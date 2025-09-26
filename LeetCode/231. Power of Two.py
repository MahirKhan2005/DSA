class Solution(object):
    # Loop version - TC - O(logn), SC - O(1)
    def isPowerOfTwo(self, n):
        while n>0:
            if n==1:
                return True
            if n%2!=0:
                return False
            n//=2
        return False

    # Bit manipulation 1 liner - TC,SC - O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n>0 and (n & (n-1)==0) else False
        
a = Solution()
print(a.isPowerOfTwo(3))