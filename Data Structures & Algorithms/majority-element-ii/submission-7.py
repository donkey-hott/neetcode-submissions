class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)

        for n in nums:
            candidates[n] += 1

            if len(candidates) > 3:
                for k in list(candidates.keys()):
                    candidates[k] -= 1

                    if candidates[k] == 0:
                        del candidates[k]
        
        counts = defaultdict(int)
        ans = []

        for n in nums:
            if n in candidates: counts[n] += 1
            if n not in ans and counts[n] > len(nums) // 3:
                ans.append(n)
        return ans
