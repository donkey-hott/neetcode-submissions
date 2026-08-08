class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        l = 0
        r = 1

        while r < len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                del nums[r]
            l += 1
            r += 1
        return len(nums)

