class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        st = []
        br_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        opening_br = br_map.values()

        for c in s:
            if c in opening_br:
                st.append(c)
            else:
                if len(st) == 0: return False
                recent_opening = st.pop()
                if recent_opening != br_map[c]: return False
        return len(st) == 0