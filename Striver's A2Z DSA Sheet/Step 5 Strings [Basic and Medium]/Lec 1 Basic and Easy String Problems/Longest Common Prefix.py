class Solution:
    def longestCommonPrefix(self, strs):
        minStr = strs[0]
        for string in strs:
            if len(string)<len(minStr):
                minStr = string
            
        i = 0
        while i<len(strs):
            if minStr=="":
                return minStr
            string = strs[i]
            if not string.startswith(minStr):
                minStr = minStr[:-1]
                i = 0
            else:
                i+=1
        return minStr

a = Solution()
print(a.longestCommonPrefix(['flower','flow','flight']))
            
                


        