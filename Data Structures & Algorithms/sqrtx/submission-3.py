class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        l, r = 1, x
        ans = 0

        while l <= r:
            m = (l + r) // 2

            if m * m > x:
                r = m - 1
            else:
                ans = m
                l = m + 1
 
        return ans