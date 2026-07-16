import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            
            lo, hi = l, l

            while hi < r:
                if nums[hi] < nums[r]:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                    lo += 1
                hi += 1
            nums[lo], nums[r] = nums[r], nums[lo]

            return lo

        def quicksort(nums, l, r):
            if l > r: return

            pivot = partition(nums, l, r)
            quicksort(nums, l, pivot - 1)
            quicksort(nums, pivot + 1, r)
        
        quicksort(nums, 0, len(nums) - 1)
        return nums