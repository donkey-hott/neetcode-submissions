class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                length = 0
                current = n

                while current in nums_set:
                    current += 1
                    length += 1
                ans = max(ans, length)
        return ans