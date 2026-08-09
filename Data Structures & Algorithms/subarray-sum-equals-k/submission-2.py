class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        counts = { 0: 1 }
        ans = 0 

        for n in nums:
            prefix_sum += n
            target = prefix_sum - k
            ans += counts.get(target, 0)
            counts[prefix_sum] = counts.get(prefix_sum, 0) + 1
        return ans