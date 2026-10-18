class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        most_frequent = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            hm[s[r]] += 1
            most_frequent = max(most_frequent, hm[s[r]])
            if (r - l + 1) - most_frequent > k:
                hm[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans