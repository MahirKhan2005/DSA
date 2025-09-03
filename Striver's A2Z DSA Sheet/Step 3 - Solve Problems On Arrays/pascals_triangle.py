class Solution(object):
    def generate(self, numRows):
        ans = []
        for i in range(0,numRows):
            inlist = []
            ans.append(inlist)
        for i in range(0,len(ans)):
            ans[i].append(1)
            if i==1:
                ans[i].append(1)
            elif i>1:
                for j in range(0,len(ans[i-1])-1):
                    ans[i].append(ans[i-1][j]+ans[i-1][j+1])
                ans[i].append(1)
    
        return ans

a = Solution()
print(a.generate(5))


