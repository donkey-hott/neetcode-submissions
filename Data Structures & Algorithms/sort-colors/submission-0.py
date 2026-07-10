class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        r = 0

        while r < len(nums):
            if nums[r] == 0:
                nums[r], nums[i] = nums[i], nums[r]
                i += 1
            r += 1
        r = i

        while r < len(nums):
            if nums[r] == 1:
                nums[r], nums[i] = nums[i], nums[r]
                i += 1
            r += 1
