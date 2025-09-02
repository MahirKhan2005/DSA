class Solution(object):
    def spiralOrder(self, matrix):
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        ans = []

        while top<=bottom and left<=right:
            # For top row
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            # For right column
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1
            # For bottom row
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            # For left column
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
                left+=1

        return ans
    
a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))