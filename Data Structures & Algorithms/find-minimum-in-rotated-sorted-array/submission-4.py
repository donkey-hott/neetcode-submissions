class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = math.inf

        while l <= r:
            m = (l + r) // 2
            ans = min(ans, nums[m])

            if nums[r] > nums[l]:
                return min(ans, nums[l])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return int(ans)