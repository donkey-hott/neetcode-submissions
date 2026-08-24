class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        adjusted_k = k % len(nums)

        i = 0

        while i < adjusted_k:
            j = len(nums) - 1

            while j > 0:
                nums[j], nums[j-1]  = nums[j-1], nums[j]
                j -= 1
            i += 1