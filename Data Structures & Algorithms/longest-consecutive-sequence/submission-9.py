class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0


        for n in nums_set:
            if n - 1 not in nums_set:
                length = 0
                count = n

                while count in nums_set:
                    length += 1
                    count += 1
                ans = max(ans, length)
        return ans
