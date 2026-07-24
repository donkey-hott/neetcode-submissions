class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        col_hashmap = [[0] * (size + 1) for _ in range(size)]
        row_hashmap = [[0] * (size + 1) for _ in range(size)]
        square_hashmap = [[0] * (size + 1) for _ in range(size)] 

        for r in range(size):
            for c in range(size):
                num = int(board[r][c]) if board[r][c] != "." else board[r][c]
                if num == ".": continue
                
                col_hashmap[c][num] += 1
                row_hashmap[r][num] += 1
                square_idx = (r // 3) * 3 + c // 3
                square_hashmap[square_idx][num] += 1

                if col_hashmap[c][num] > 1 or row_hashmap[r][num] > 1 or square_hashmap[square_idx][num] > 1: return False
        return True