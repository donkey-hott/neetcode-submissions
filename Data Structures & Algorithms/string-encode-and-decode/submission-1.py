class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            prefix = f':{len(s)}:'
            output += prefix

            for char in s:
                output += char
        return output

    def decode(self, s: str) -> List[str]:
        word_len = 0
        i = 0
        decoded = []
        while i < len(s):
            if s[i] == ':':
                p = i + 1
                while s[p] != ':':
                    p += 1
                word_len = int(s[i+1:p])
                i = p + 1

            word = ''
            while len(word) < word_len:
                word += s[i]
                i += 1
            decoded.append(word)
        return decoded
