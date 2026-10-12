class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        slowest = 0
        ans = 0

        for pos, spd in cars:
            t = (target - pos) / spd

            if t > slowest:
                ans += 1
                slowest = t
        return ans




