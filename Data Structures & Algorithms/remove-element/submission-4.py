class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        k = 0
        while (l < len(nums)):
            while nums[l] == val:
                if r < l: return l
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                k += 1
            l += 1
        return len(nums) - k