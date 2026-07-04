class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            k = str(key)
            if k not in hashmap:
                hashmap[k] = []
            hashmap[k].append(word)
        return list(hashmap.values())