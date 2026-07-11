class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for n in nums:
            frequencies[n] += 1
        
        tuples = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

        ans = []
        i = 0
        while len(ans) < k:
            ans.append(tuples[i][0])
            i += 1
        return ans