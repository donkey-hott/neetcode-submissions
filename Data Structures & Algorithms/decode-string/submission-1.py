class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def decode(start: int):
            i = start
            ans = ''
            while i < n and s[i] != ']':
                if s[i].isdigit():
                    r = i
                    while s[r].isdigit():
                        r += 1
                    
                    count = int(s[i:r])
                    string, idx = decode(r + 1)

                    for _ in range(count):
                        ans += string
                    i = idx + 1
                else:
                    ans += s[i]
                    i += 1
            return (ans, i)
        return decode(0)[0]