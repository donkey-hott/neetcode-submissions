class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)

        for n in nums:
            hm[n] += 1

            if len(hm) > 2:
                for k in list(hm.keys()):
                    hm[k] -= 1

                    if hm[k] == 0:
                        del hm[k]
        
        count = defaultdict(int)
        ans = []

        for n in nums:
            count[n] += 1
            if n in hm and n not in ans and count[n] > len(nums) // 3:
                ans.append(n)
        return ans