# TC - O(n), SC - O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapS,mapT = {},{}
        for chS,chT in zip(s,t):
            mapS[chS] = mapS.get(chS,0) + 1
            mapT[chT] = mapT.get(chT,0) + 1
        for ch in mapS:
            if (ch in mapT and mapS[ch]!=mapT[ch]) or ch not in mapT:
                return False
        for ch in mapT:
            if (ch in mapS and mapT[ch]!=mapS[ch]) or ch not in mapS:
                return False
        return True

# TC - O(n), SC - O(n) - Same approach but less code
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapS,mapT = {},{}
        for chS,chT in zip(s,t):
            mapS[chS] = mapS.get(chS,0) + 1
            mapT[chT] = mapT.get(chT,0) + 1
        return mapS==mapT
    
# TC - O(nlogn), SC - O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s==t