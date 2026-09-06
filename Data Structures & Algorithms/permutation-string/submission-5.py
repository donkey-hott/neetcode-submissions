class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequencies = {}
        l, n = 0, len(s2)

        for c in s1:
            frequencies[c] = frequencies.get(c, 0) + 1
        
        for l in range(n):
            if s2[l] in frequencies:
                frequencies_c = {}
                for r in range(l, min(l + len(s1), len(s2))):
                    frequencies_c[s2[r]] = frequencies_c.get(s2[r], 0) + 1

                if frequencies == frequencies_c:
                    return True
        return False