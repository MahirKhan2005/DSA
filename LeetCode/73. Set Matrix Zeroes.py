class Solution(object):
    def setZeroes(self, matrix):
        # Flags if the first row has a zero
        first_row_zero = False
        first_column_zero = False
        for j in range(0,len(matrix[0])):
            if matrix[0][j]==0:
                first_row_zero = True

        # Flags if the first column has a zero
        for i in range(0,len(matrix)):
            if matrix[i][0]==0:
                first_column_zero = True

        # Iterates the whole matrix, if any element come out to be zero then mark the frist element of its column and row to zero
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Now Again iteration and change 1's with 0's whos column or row has their first element to be 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        
        # For the first column
        if first_column_zero:
            for i in range(0,len(matrix)):
                matrix[i][0] = 0

        # For the first row
        if first_row_zero:
            for j in range(0,len(matrix[0])):
                matrix[0][j]=0
        


a = Solution()
print(a.setZeroes( [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

        