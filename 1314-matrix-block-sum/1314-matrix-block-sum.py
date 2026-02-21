class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        nummat = NumMatrix(mat)
        resmat = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x1 = max(i-k,0)
                y1 = max(j-k, 0)

                x2 = min(i+k,m-1)
                y2 = min(j+k, n-1) 
                resmat[i][j] = nummat.sumRegion(x1, x2, y1, y2)
        return resmat

class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0] * (n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1]= self.prefix[i][j+1] + self.prefix[i+1][j] - self.prefix[i][j] + matrix[i][j]
    
    def sumRegion(self, x1, x2, y1, y2):
        return self.prefix[x2+1][y2+1] - self.prefix[x1][y2+1] - self.prefix[x2+1][y1] + self.prefix[x1][y1] 