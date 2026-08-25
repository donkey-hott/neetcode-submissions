class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                length = 0
                cur = n

                while cur in nums_set:
                    length += 1
                    cur += 1
                ans = max(length, ans)
        return ans