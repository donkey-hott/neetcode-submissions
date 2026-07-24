class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        col_hashmap = [[False] * (size + 1) for _ in range(size)]
        row_hashmap = [[False] * (size + 1) for _ in range(size)]
        square_hashmap = [[False] * (size + 1) for _ in range(size)] 

        for r in range(size):
            for c in range(size):
                if board[r][c] == ".": continue
                num = int(board[r][c])
                square_idx = (r // 3) * 3 + c // 3
                if col_hashmap[c][num] or row_hashmap[r][num] or square_hashmap[square_idx][num]: return False
                
                col_hashmap[c][num] = True
                row_hashmap[r][num] = True
                square_hashmap[square_idx][num] = True

        return True