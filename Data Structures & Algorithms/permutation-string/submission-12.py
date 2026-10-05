class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if n < m: return False
        need = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1
        
        have = [0] * 26

        for i in range(m):
            have[ord(s2[i]) - ord('a')] += 1
        
        if have == need: return True

        for i in range(m, n):
            have[ord(s2[i]) - ord('a')] += 1
            have[ord(s2[i - m]) - ord('a')] -= 1
            if have == need: return True
        return False
