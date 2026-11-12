class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        ans = nums[l]

        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                return min(ans, nums[l])
            
            ans = min(ans, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ans
