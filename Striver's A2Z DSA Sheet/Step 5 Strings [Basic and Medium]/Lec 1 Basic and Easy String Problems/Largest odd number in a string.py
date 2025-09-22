class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""

a = Solution()
print(a.largestOddNumber("90999"))