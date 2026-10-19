class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bisect(row: List[int]) -> bool:
            l, r = 0, len(row) - 1

            while l < r:
                m = (l + r) // 2

                if target > row[m]:
                    l = m + 1
                else:
                    r = m
            return True if (l < len(row) and row[l] == target) else False
        
        for row in matrix:
            exists = bisect(row)
            if exists: return True
        return False