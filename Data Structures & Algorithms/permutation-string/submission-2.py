class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequencies = defaultdict(int)
        l, n = 0, len(s2)

        for c in s1:
            frequencies[c] += 1
        
        while l < n:
            if s2[l] in frequencies:
                r = l
                frequencies_c = frequencies.copy()
                while r < n and s2[r] in frequencies_c and frequencies_c[s2[r]] > 0:
                    frequencies_c[s2[r]] -= 1
                    r += 1

                if all(v == 0 for v in frequencies_c.values()):
                    return True
            l += 1
        return False