class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            complement = target - nums[l]

            while r > l and nums[r] > complement:
                r -= 1
            if nums[r] == complement:
                return [l+1, r+1]
            
            l += 1

        return []