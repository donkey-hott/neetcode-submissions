class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        i, length = 0, len(nums)
        while i < length:
            l, r = i + 1, length - 1

            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1

                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
            i += 1

            while i < length and nums[i-1] == nums[i]:
                i += 1
        return ans