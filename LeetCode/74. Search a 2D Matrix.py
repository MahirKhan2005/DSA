class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        
        start,end = 0,m-1
        row = -1
        while start<=end:
            mid = start + (end-start)//2
            if target<matrix[mid][0]:
                end = mid - 1
            elif target>matrix[mid][-1]:
                start = mid + 1
            else:
                row = mid 
                break
        if row==-1:
            return False
            
        
        start, end = 0,n-1
        while start<=end:
            mid = start + (end-start)//2
            if target==matrix[row][mid]:
                return True
            elif target<matrix[row][mid]:
                end = mid - 1
            else:
                start = mid + 1
        return False