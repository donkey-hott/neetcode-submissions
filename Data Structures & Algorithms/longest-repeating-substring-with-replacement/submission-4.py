class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        most_frequent_count = 0
        ans = 0
        r = l = 0

        while r < len(s):
            frequencies[s[r]] += 1
            most_frequent_count = max(most_frequent_count, frequencies[s[r]])
            while (r - l + 1) - most_frequent_count > k:
                frequencies[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
