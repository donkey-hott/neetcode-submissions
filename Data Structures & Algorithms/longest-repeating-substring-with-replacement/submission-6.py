class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        frequencies = defaultdict(int)
        most_frequent = 0
        l = 0

        for r in range(len(s)):
            frequencies[s[r]] += 1
            most_frequent = max(most_frequent, frequencies[s[r]])
            
            if (r - l + 1) - most_frequent > k:
                frequencies[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans

