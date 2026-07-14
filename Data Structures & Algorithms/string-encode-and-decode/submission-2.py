class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            prefix = f'{len(s)}:'
            encoded += prefix

            for char in s:
                encoded += char
        return encoded

    def decode(self, s: str) -> List[str]:
        word_len = 0
        i = 0
        decoded = []
        while i < len(s):
            p = i
            while s[p] != ':':
                p += 1
            word_len = int(s[i:p])

            i = p + 1
            word = ''
            
            while len(word) < word_len:
                word += s[i]
                i += 1
            decoded.append(word)
        return decoded
