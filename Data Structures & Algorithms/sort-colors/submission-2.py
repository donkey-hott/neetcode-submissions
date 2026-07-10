class Solution:
    def sortColors(self, nums: List[int]) -> None:
        t = len(nums) - 1
        o = 0
        r = 0

        while r <= t:
            if nums[r] == 0:
                nums[r], nums[o] = nums[o], nums[r]
                o += 1
                r += 1
            elif nums[r] == 2:
                nums[r], nums[t] = nums[t], nums[r]
                t -= 1
            else: r += 1