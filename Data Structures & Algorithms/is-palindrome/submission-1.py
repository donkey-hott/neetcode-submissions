import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        is_alphanumeric = r"[A-Za-z0-9]+"
        while l < r:
            while not re.fullmatch(is_alphanumeric, s[l]) and l < len(s) - 1: l += 1
            while not re.fullmatch(is_alphanumeric, s[r]) and r >= 0: r -= 1

            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True
    