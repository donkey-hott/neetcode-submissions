class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += (str(len(s)) + ":" + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        decoded = []

        while i < n:
            j = i

            while s[j] != ':':
                j += 1
            length = int(s[i:j])
            j += 1
            decoded.append(s[j:j+length])
            i = j + length
        return decoded
