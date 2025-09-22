class Solution:
    # TC - O(n^2) due to this ans+=s[start+1:end], SC - O(n)
    def removeOuterParentheses(self, s: str) -> str:
        start = 0
        ans = ""
        left = 0
        right = 0
        for end in range(0,len(s)):
            if s[end]=="(":
                left+=1
            elif s[end]==")":
                right+=1
            if left==right:
                ans+=s[start+1:end]
                left=0
                right=0
                start = end+1
        return ans

# TC - O(n), SC - O(n)
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        depth = 0
        for ch in s:
            if ch=="(":
                if depth>0:
                    ans.append(ch)
                depth+=1
            else:
                depth-=1
                if depth>0:
                    ans.append(ch)
        return "".join(ans)


a = Solution()
print(a.removeOuterParentheses("(()())(())"))

        