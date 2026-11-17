class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = self._createPrefix(matrix)

    def _createPrefix(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(rows):
            for col in range(cols):
                prefix[row+1][col+1] = (matrix[row][col] + prefix[row][col+1] + prefix[row+1][col]) - prefix[row][col]
        return prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1]) + self.prefix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)