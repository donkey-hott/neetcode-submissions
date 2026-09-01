class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        n = len(s)
        hashmap = set()

        while r < n:
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
            hashmap.add(s[r])
            ans = max(ans, (r - l) + 1)
            r += 1
        return ans