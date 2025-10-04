class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s)==1 and s!=' ':
            return 1
        i=-1
        length = 0
        # Skipping trailing white spaces
        while s[i]==' ':
            i-=1
        while i>=-len(s) and s[i]!=' ':
            length+=1
            i-=1
        return length