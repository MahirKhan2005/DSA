# TC - O(n^2), SC - O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        string = s
        for _ in range(len(goal)):
            string = list(string)
            ch = string.pop(0)
            string.append(ch)
            string = "".join(string)
            if string==goal:
                return True
        return False
    

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        return goal in (s+s)



a = Solution()
print(a.rotateString('abcde','cdeab'))