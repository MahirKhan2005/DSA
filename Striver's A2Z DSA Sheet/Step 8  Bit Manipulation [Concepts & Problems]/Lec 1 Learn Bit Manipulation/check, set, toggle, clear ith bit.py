class Solution:
    def checkIthBit(self, n: int, i: int) -> bool:
        return True if (n>>i) & 1 else False
    
    def setIthBit(self, n: int, i: int):
        return n | (1<<i)

    def toggleIthBit(self, n: int, i: int):
        return n ^ (1<<i)

    def clearIthBit(self, n: int, i: int) -> int:
        return n & ~(1<<i)

a = Solution()
print(a.checkIthBit(10,3))
print(a.setIthBit(10,2))
print(a.toggleIthBit(10,1))
print(a.clearIthBit(10,3))