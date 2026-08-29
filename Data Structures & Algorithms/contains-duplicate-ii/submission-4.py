class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = set()
        start = 0
        end = 0
        n = len(nums)
    
        while end < n:
            if nums[end] in hashmap: return True
            hashmap.add(nums[end])
            
            if end - start == k:
                hashmap.remove(nums[end-k])
                start += 1

            end += 1
        return False