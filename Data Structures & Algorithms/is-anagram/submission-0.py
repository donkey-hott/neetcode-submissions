class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hash_map = {}

        for s_char in s:
            hash_map[s_char] = hash_map.get(s_char, 0) + 1
        for t_char in t:
            if t_char not in hash_map: return False
            hash_map[t_char] -= 1
        return all(item == 0 for item in hash_map.values())