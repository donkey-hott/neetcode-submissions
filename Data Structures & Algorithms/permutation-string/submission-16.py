class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        if n2 < n1: return False

        need = [0] * 26

        for char in s1:
            need[ord(char) - ord('a')] += 1

        have = [0] * 26

        for i in range(n1):
            have[ord(s2[i]) - ord('a')] += 1
        
        if have == need: return True

        for i in range(n1, n2):
            if have == need: return True
            have[ord(s2[i]) - ord('a')] += 1
            have[ord(s2[i - n1]) - ord('a')] -= 1
        
        return have == need
