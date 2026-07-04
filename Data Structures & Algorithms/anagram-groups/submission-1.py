class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            hashmap[str(key)].append(word)
        return list(hashmap.values())