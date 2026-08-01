class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        ex_prefix_sums = { 0: 1 }
        ans = 0
        for n in nums:
            prefix_sum += n
            ans += ex_prefix_sums.get(prefix_sum - k, 0)
            ex_prefix_sums[prefix_sum] = ex_prefix_sums.get(prefix_sum, 0) + 1
        return ans
