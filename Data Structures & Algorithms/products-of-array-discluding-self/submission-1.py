class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1] * (l + 1)
        suffix = [1] * (l + 1)

        for i in range(l):
            prefix[i+1] = nums[i] * prefix[i]
            suffix[i+1] = nums[l - i - 1] * suffix[i]

        ans = []
        for j in range(l):
            ans.append(prefix[j] * suffix[l - j - 1])
        return ans