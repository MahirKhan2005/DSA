class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        while n>0:
            if n:
                even+=n&1
                n>>=1
            if n:
                odd+=n&1
                n>>=1
        return [even,odd]