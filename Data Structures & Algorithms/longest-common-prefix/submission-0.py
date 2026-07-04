class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i,char in enumerate(strs[0]):
            matches = all(i < len(w) and w[i] == char for w in strs)
            if not matches: return ans
            ans += char
        return ans