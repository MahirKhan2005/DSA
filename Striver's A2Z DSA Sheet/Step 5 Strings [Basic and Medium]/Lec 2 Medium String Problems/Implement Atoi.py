class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        ans = 0
        sign = 1
        n = len(s)
        # Skip leading spaces
        while i<n and s[i]==" ":
            i+=1

        # Sign check
        if i<n and (s[i]=="-" or s[i]=="+"):
            sign = -1 if s[i]=="-" else 1
            i+=1

        # Skipping leading zeros
        while i<n and s[i]=="0":
            i+=1

        # Reading through the remaining characters
        while i<n and s[i].isdigit():
            ans = ans*10 + int(s[i])
            i+=1

        ans*=sign
        # Round off if out of bounds
        INT_MIN,INT_MAX = -2**31,2**31-1
        if ans<INT_MIN:
            return INT_MIN
        elif ans>INT_MAX:
            return INT_MAX

        return ans

a = Solution()
print(a.myAtoi('  -042890sda89'))