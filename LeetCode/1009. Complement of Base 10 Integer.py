class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        num = n
        xor = 0
        while num>0:
            num>>=1
            xor<<=1
            xor^=1
        return n^xor