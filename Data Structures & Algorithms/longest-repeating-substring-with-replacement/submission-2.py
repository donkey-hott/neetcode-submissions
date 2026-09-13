class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_frequency = 0
        l, n = 0, len(s)
        ans = 0

        for r in range(n):
            counts[s[r]] += 1

            max_frequency = max(max_frequency, counts[s[r]])

            if (r - l + 1) - max_frequency > k:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans