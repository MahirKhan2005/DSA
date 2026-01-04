class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        i=0
        j=len(s)-1
        ans1=ans2=True
        while i<j:
            if s[i]!=s[j]:
                temp1 = s[:]
                temp2 = s[:]
                temp1.pop(i)
                temp2.pop(j)
                i1=i2=0
                j1=j2=len(temp1)-1
                while i1<j1:
                    if temp1[i1]!=temp1[j1]:
                        ans1 = False
                    i1+=1
                    j1-=1
                while i2<j2:
                    if temp2[i2]!=temp2[j2]:
                        ans2 = False
                    i2+=1
                    j2-=1
                return ans1 or ans2
            i+=1
            j-=1
        return True
            
                