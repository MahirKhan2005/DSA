class Solution(object):
    def rotate(self, matrix):
        # Transposing the matrix
        for i in range(0,len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        # Reversing the rows
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)//2):
                matrix[i][j],matrix[i][len(matrix)-1-j] = matrix[i][len(matrix)-1-j],matrix[i][j]
        return matrix

a = Solution()
print(a.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(a.rotate([[1,2,3],[4,5,6],[7,8,9]]))