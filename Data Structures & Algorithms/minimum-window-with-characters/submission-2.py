class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)

        if n < m: return ""
        t_hm, window_hm = {}, {}
        l = 0
        for c in t:
            t_hm[c] = t_hm.get(c, 0) + 1
        ans, ans_len = [-1, -1], float("infinity")
        have, need = 0, len(t_hm)

        for r,c in enumerate(s):
            window_hm[c] = window_hm.get(c, 0) + 1

            if c in t_hm and window_hm[c] == t_hm[c]:
                have += 1
            while have == need:
                if r - l + 1 < ans_len:
                    ans = [l, r]
                    ans_len = r - l + 1
                window_hm[s[l]] -= 1
                if s[l] in t_hm and window_hm[s[l]] < t_hm[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        return s[l:r+1] if ans_len != float("infinity") else ""