# TC,SC - O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i=len(s)-1
        while i>=0:
            # Skips spaces
            while i>=0 and s[i]==" ":
                i-=1
            # Edge case if there are leading spaces
            if i<0:
                break
            # End of the word
            j=i
            while i>=0 and s[i]!=" ":
                i-=1
            # Appending the word
            ans.append(s[i+1:j+1])
        return " ".join(ans)


# TC,SC - O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])