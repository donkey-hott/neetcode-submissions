from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(k: int) -> int:
            return sum(ceil(p / k) for p in piles)

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if hours_needed(m) <= h:   # feasible: try slower
                r = m
            else:                      # too slow
                l = m + 1
        return l