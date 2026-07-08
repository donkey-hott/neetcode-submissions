class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            hashmap = [0] * 26
            for i, char in enumerate(s):
                hashmap[ord(char) - ord('a')] += 1
            groups[str(hashmap)].append(s)

        return list(groups.values())