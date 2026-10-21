class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            else:
                r = m
        return l + 1 if target > nums[l] else l