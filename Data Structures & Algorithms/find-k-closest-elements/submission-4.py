import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        closest_idx = bisect.bisect_left(arr, x)
        l, r = closest_idx - 1, closest_idx

        while r - l - 1 < k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
        return arr[l + 1:r]