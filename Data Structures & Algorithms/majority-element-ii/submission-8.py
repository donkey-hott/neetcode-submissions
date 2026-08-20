class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = defaultdict(int)

        for n in nums:
            candidates[n] += 1

            if len(candidates) > 2:
                for key in list(candidates.keys()):
                    candidates[key] -= 1

                    if candidates[key] == 0:
                        del candidates[key]

        counts = defaultdict(int)
        ans = []

        for n in nums:
            if n in candidates: counts[n] += 1
            if counts[n] > len(nums) // 3 and n not in ans: ans.append(n)
        return ans