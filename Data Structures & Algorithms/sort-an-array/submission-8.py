import random

class Solution:

    def _partition(self, nums: List[int], start: int, end: int):
        pivot_idx = random.randint(start, end)
        nums[end], nums[pivot_idx] = nums[pivot_idx], nums[end]
        l, r = start, start

        while r < end:
            if nums[r] < nums[end]:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1
        
        nums[l], nums[end] = nums[end], nums[l]
        return l


    def _quicksort(self, nums: List[int], l: int, r: int):
        if l > r: return nums
        pivot = self._partition(nums, l, r)

        self._quicksort(nums, l, pivot - 1)
        self._quicksort(nums, pivot + 1, r)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self._quicksort(nums, 0, len(nums) - 1)