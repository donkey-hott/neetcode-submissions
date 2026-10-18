class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            while l < n and s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            ans = max(ans, r - l + 1)
        return ans