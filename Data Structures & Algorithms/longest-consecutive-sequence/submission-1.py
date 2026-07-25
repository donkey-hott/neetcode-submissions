class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                current_num = n
                length = 1

                while current_num + 1 in nums_set:
                    length += 1
                    current_num += 1
                ans = max(length, ans)
        return ans