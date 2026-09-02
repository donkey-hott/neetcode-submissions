class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l, r = 0, 0
        ans = 0

        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            ans = max(ans, r - l + 1)
            hs.add(s[r])
            r += 1
        return ans
