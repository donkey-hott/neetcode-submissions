class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ans = math.inf

        while l <= r:
            m = (l + r) // 2
            ans = min(ans, nums[m])

            if nums[r] < nums[l] and nums[r] < nums[m]:
                l = m + 1
            elif nums[l] < nums[r] and nums[r] < nums[m]:
                r = m - 1
            elif m > 0 and m < n - 1 and nums[m-1] > nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return int(ans)