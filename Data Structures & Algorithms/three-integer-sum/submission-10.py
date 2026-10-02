class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        n = len(nums)

        while i < n:
            l, r = i + 1, n - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum < 0:
                    l += 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
            i += 1
            while i < n and nums[i] == nums[i - 1]:
                i += 1
        return ans
