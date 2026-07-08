class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,n in enumerate(nums):
            complement = target - n
            if n in hashmap:
                return [hashmap[n],i]
            hashmap[complement] = i
        return []