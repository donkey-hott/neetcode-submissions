import random

class Solution:
    def partition(self, nums: List[int], lo: int, hi: int):
        pivot_idx = random.randint(lo,hi)
        nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
        l, r = lo, lo

        while r < hi:
            if nums[r] < nums[hi]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        nums[l], nums[hi] = nums[hi], nums[l]
        return l

    def quicksort(self, nums: List[int], l: int, r: int):
        if l > r: return

        pivot = self.partition(nums, l, r)
        self.quicksort(nums, l, pivot - 1)
        self.quicksort(nums, pivot + 1, r)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums