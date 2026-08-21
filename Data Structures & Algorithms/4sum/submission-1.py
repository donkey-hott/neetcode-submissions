class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        length = len(nums)
        i = 0
        ans = []

        while i < length:
            ii = i + 1
            inter_target = target - nums[i]

            while ii < length:
                l, r = ii + 1, length - 1

                while l < r:
                    cur_sum = nums[ii] + nums[l] + nums[r]

                    if cur_sum < inter_target:
                        l += 1
                    elif cur_sum > inter_target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[ii], nums[l], nums[r]])
                        l, r = l + 1, r - 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                ii += 1

                while ii < length and nums[ii] == nums[ii - 1]:
                    ii += 1
            i += 1

            while i < length and nums[i] == nums[i - 1]:
                i += 1

        return ans