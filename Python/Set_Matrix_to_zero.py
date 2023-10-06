class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])

        row=[False]*n
        col=[False]*m

        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True

        for i in range(0,n):
            for j in range(0,m):
                if (row[i] or col[j]):
                    matrix[i][j]=0

        return matrix
