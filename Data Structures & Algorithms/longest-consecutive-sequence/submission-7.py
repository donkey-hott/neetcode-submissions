class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        ans = 0

        for n in nums:
            if n - 1 not in hs:
                cur = n + 1
                length = 1

                while cur in hs:
                    length += 1
                    cur += 1
                ans = max(ans, length)
        return ans