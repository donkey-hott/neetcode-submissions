class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        row_l, row_r = 0, rows - 1

        # find the row

        while row_l < row_r:
            m = (row_l + row_r) // 2

            if target > matrix[m][-1]:
                row_l = m + 1
            else:
                row_r = m

        # find the cell
        col_l, col_r = 0, cols - 1

        while col_l < col_r:
            m = (col_l + col_r) // 2

            if target > matrix[row_l][m]:
                col_l = m + 1
            else:
                col_r = m
        return True if (col_l < cols and matrix[row_l][col_l] == target) else False

