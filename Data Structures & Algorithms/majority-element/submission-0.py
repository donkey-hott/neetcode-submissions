class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
            if hashmap[n] > len(nums) // 2: return n

        return -1