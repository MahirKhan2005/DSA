class Solution:
    def isOdd(self, n: int) -> bool:
        return True if n & 1 else False

a = Solution()
print(a.isOdd(8))