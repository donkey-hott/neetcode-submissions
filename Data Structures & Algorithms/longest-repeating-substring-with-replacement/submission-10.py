class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        most_frequent = 0
        ans = 0
        l = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            most_frequent = max(most_frequent, chars[s[r]])
            while (r - l + 1) - most_frequent > k:
                chars[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans