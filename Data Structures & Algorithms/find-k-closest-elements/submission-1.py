class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1

        while r - l + 1 > k:
            l_distance, r_distance = abs(arr[l] - x), abs(arr[r] - x)

            if l_distance < r_distance or (l_distance == r_distance and arr[l] < arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l:r+1]