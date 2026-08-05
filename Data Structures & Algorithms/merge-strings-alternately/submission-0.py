class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        longest = max(l1, l2)
        i = 0
        ans = ""

        while i < longest:
            if i < l1:
                ans += word1[i]
            if i < l2:
                ans += word2[i]
            i += 1
        
        return ans