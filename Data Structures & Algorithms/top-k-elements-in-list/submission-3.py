import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for n in nums:
            frequencies[n] += 1
        
        q = []
        for key in frequencies:
            heapq.heappush(q, (frequencies[key], key))
            if len(q) > k:
                heapq.heappop(q)

        ans = []
        
        for i in range(k):
            _, value = heapq.heappop(q)
            ans.append(value)
        return ans

