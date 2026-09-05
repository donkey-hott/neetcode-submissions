class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, ans = 0, 0
        hm = defaultdict(int)
        max_frequency = 0

        for r in range(len(s)):
            hm[s[r]] += 1
            max_frequency = max(max_frequency, hm[s[r]])

            if (r - l + 1) - max_frequency > k:
                hm[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans