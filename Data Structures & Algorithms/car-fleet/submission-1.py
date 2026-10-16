class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        slowest = 0
        ans = 0

        for c in cars:
            p, s = c

            t = (target - p) / s

            if t > slowest:
                slowest = t
                ans += 1
        return ans