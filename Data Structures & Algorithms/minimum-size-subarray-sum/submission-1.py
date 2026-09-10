class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = 0
        n = len(nums)
        s_sum = 0

        for r in range(n):
            s_sum += nums[r]
            while s_sum >= target:
                ans = r - l + 1 if ans == 0 else min(ans, r - l + 1)
                s_sum -= nums[l]
                l += 1
        return ans