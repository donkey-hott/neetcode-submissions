class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
            if len(hashmap) > 2:
                for k in list(hashmap.keys()):
                    hashmap[k] -= 1

                    if hashmap[k] == 0:
                        del hashmap[k]
        
        res = []
        for n in hashmap:
            if nums.count(n) > len(nums) // 3:
                 res.append(n)
        return res