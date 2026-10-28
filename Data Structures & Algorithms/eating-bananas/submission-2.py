from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        
        while l < r:
            k = (l + r) // 2
            total = 0

            for p in piles:
                total += ceil(p / k)
                if total > h:
                    l = k + 1
                    break

            if total <= h:
                r = k
        return l