class Solution:
    def getRow(self, rowIndex: int):
        r = rowIndex
        if r==0:
            return [1]
        prev = [1,1]
        for i in range(r-1):
            next = [1]
            for j in range(len(prev)-1):
                next.append(prev[j]+prev[j+1])
            next.append(1)
            prev = next
        return prev

