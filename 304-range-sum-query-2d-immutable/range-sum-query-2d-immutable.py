class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = [[0]*(len(matrix[0])+1) for i in range (len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.mat[i][j+1] += matrix[i][j] + self.mat[i][j]
        print(self.mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.sum = 0
        for i in range(row1, row2+1):
            self.sum += self.mat[i][col2+1] - self.mat[i][col1]
        return self.sum
        # self.mat[row1][col2+1] - self.mat[row1][col1] + self.mat[row2][col2+1] - self.mat[row2][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)