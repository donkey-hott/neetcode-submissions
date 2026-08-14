class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, length = 0, len(nums)
        ans = []

        while i < length:
            while i > 0 and i < length -1 and nums[i] == nums[i-1]:
                i += 1
            if i == length - 1: return ans
            l,r = i+1, length-1

            while l<r:
                cur_sum = nums[i] + nums[l] + nums[r]

                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[r], nums[l]])
                    l += 1
                    r -= 1

                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r+1] == nums[r]:
                        r -= 1
            i += 1
        return ans
        


            
