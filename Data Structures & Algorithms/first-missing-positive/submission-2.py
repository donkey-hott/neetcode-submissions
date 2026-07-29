class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)

        for i in range(l):
            while 1 <= nums[i] <= l and nums[nums[i] - 1] != nums[i]:
                t = nums[i] - 1
                nums[i], nums[t] = nums[t], nums[i]
        
        for i in range(l):
            if nums[i] != i + 1:
                return i + 1
        return l + 1