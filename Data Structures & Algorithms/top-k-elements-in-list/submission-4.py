class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)

        # count frequencies of each integer
        frequencies = defaultdict(int)
        for n in nums:
            frequencies[n] += 1

        # create an array with buckets of `nums` length + 1
        buckets = [[] for _ in range(l + 1)]

        # arrange numbers by buckets based on frequency of each of them
        for num in frequencies:
            buckets[frequencies[num]].append(num)
        
        ans = []
        # populate the `ans` list by walking from highest frequency
        # to lowest and pulling out integers from their buckets
        for frequency in range(l, 0, -1):
            for i in buckets[frequency]:
                ans.append(i)
                if len(ans) == k:
                    return ans
        return ans