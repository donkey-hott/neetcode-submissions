class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        ans = set()
        target = len(nums) // 3

        for n in nums:
            hashmap[n] += 1
            if hashmap[n] > target: ans.add(n)
        return list(ans)