class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        st = []
        br_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in br_map:
                if len(st) == 0: return False
                recent_opening = st.pop()
                if recent_opening != br_map[c]: return False
            else:
                st.append(c)
        return len(st) == 0