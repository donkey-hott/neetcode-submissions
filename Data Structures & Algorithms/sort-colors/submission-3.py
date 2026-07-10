class Solution:
    def sortColors(self, nums: List[int]) -> None:
        t = len(nums) - 1
        o = 0
        r = 0
        while o <= r <= t:
            if nums[r] == 0:
                nums[r], nums[o] = nums[o], nums[r]
                o += 1
            if nums[r] == 2:
                nums[r], nums[t] = nums[t], nums[r]
                t -= 1
                continue
            r += 1