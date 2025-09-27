# TC - O(logn)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if 1 & n:
                count+=1
            n>>=1
        return count

# Brian Kernighan's Algorithm - O(logn)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1  # Unsets the rightmost set bit
            count+=1
        return count 