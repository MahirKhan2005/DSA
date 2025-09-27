class Solution:
    def swapNumbers(self, a: int, b: int) -> tuple:
        a^=b
        b^=a
        a^=b
        return (a,b)

a = Solution()
print(a.swapNumbers(5,10))