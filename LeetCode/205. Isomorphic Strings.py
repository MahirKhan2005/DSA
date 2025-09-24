class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST,mapTS = {},{}
        i = 0
        for chS,chT in zip(s,t):
            if chS in mapST and mapST[chS]!=chT:
                return False
            if chT in mapTS and mapTS[chT]!=chS:
                return False
            
            mapST[chS] = chT
            mapTS[chT] = chS
        return True

a = Solution()
print(a.isIsomorphic('paper','title'))
