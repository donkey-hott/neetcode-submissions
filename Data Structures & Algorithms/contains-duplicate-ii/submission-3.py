class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False

        def containsDuplicate(l: int, r: int) -> bool:
            hashmap = set()

            for i in range(l, r+1):
                if nums[i] in hashmap: return True
                hashmap.add(nums[i])
            return False

        start, end, n = 0, min(k, len(nums)-1), len(nums)
    
        while end < n:
            if containsDuplicate(start, end): return True
            start += 1
            end += 1
        return False

        