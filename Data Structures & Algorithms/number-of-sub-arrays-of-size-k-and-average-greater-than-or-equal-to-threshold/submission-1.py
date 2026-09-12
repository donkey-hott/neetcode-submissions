class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r, n = 0, 0, len(arr)
        ans = 0
        c_sum = 0

        while r < n:
            while r - l + 1 <= k:
                c_sum += arr[r]
                r += 1
            if c_sum // k >= threshold:
                ans += 1
            c_sum -= arr[l]
            l += 1
        return ans