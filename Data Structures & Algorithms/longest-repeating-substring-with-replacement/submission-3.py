class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        max_frequency = 0
        ans = 0
        
        l, n = 0, len(s)

        for r in range(n):
            frequencies[s[r]] += 1
            max_frequency = max(max_frequency, frequencies[s[r]])
            if (r - l + 1) - max_frequency > k:
                frequencies[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans