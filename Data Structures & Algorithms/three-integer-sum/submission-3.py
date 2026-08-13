class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        length = len(nums)
        i = 0

        while i < len(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            l, r = i + 1, length - 1
            target = -nums[i]
            while l < r:    
                cur_sum = nums[l] + nums[r]
                
                if cur_sum > target:
                    r -= 1
                elif cur_sum < target:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            i += 1
            
        return ans
