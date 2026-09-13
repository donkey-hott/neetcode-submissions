class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n: return False
        
        needed = [0] * 26
        window = [0] * 26

        for ch in s1:
            needed[ord(ch) - ord('a')] += 1
        
        for i in range(m):
            window[ord(s2[i]) - ord('a')] += 1
        
        if window == needed: return True

        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - m]) - ord('a')] -= 1

            if window == needed:
                return True
        return False