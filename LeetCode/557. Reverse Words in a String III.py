class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        i=j=0
        while i<len(s)-1 and j<len(s)-1:
            while j<len(s)-1 and s[j+1]!=' ':
                j+=1
            k=j
            while i<j:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            i=k+2
            j=i
        return "".join(s)
    
a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))