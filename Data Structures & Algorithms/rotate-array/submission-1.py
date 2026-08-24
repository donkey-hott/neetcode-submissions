class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        pivot = k - 1
        
        self._reverse(nums, 0, length - k - 1)
        self._reverse(nums, length - k, length - 1)
        self._reverse(nums, 0, length - 1)
    
    def _reverse(self, nums: List[int], start: int, end: int) -> None:
        l, r = start, end

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1