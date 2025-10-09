class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            isDividing = True
            num = i
            while num>0:
                if (num%10!=0 and i%(num%10)!=0) or num%10==0:
                    isDividing = False
                num//=10
            if isDividing:
                ans.append(i)
        return ans