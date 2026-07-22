import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, lo, hi):
            pivot_idx = random.randint(lo, hi)
            nums[hi], nums[pivot_idx] = nums[pivot_idx], nums[hi]
            l, r = lo, lo
    
            while r < hi:
                if nums[r] < nums[hi]:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                r += 1
            nums[l], nums[hi] = nums[hi], nums[l]
            return l
        
        def quicksort(nums, l, r):
            if l > r: return nums

            pivot = partition(nums, l, r)
            quicksort(nums, l, pivot - 1)
            quicksort(nums, pivot + 1, r)
            return nums
        
        return quicksort(nums, 0, len(nums) - 1)