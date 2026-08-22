class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f'{(len(s))}:{s}'
        return encoded
    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            length = 0

            while s[j] != ":":
                j += 1
            length = int(s[i:j])
 
            j += 1
            i = j + length
            decoded.append(s[j:i])

        return decoded