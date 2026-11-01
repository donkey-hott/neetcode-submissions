class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)


        ans = 0
        slowest = 0

        for pos,sp in cars:
            t = (target - pos) / sp

            if t > slowest:
                ans += 1
                slowest = t
        return ans
