class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()

        flag_row = False
        flag_col = False

        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0:
                    matrix[i][0] = 0.5
                    if i == 0:
                        flag_row = True
                    matrix[0][j] = 0.5
                    if j == 0:
                        flag_col = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0: continue
                if ( matrix[0][j] == 0.5 or matrix[i][0] == 0.5 )and (matrix[i][j] != 0.5):
                    matrix[i][j] = 0

    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if  matrix[i][j] == 0.5:
                    matrix[i][j] = 0
        if flag_row:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if flag_col:
            for r in range(len(matrix)):
                matrix[r][0] = 0