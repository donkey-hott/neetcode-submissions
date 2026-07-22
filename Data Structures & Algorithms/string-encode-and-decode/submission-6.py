class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += (str(len(s)) + ":" + s)
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        i = 0

        while i < len(s) - 1:
            j = i

            while s[j] != ":":
                j += 1

            length = int(s[i:j])
            i = j + 1
            decoded.append(s[i:length+i])
            i += length
        return decoded