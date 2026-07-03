class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hash_map = [0] * 26

        for i in range(len(s)):
            hash_map[ord(s[i]) - ord('a')] += 1
            hash_map[ord(t[i]) - ord('a')] -= 1
        return all(item == 0 for item in hash_map)