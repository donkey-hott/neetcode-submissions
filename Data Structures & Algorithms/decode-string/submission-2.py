class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        self.i = 0
    
        def decode():
            ans = ''
            while self.i < n and s[self.i] != ']':
                if s[self.i].isdigit():
                    r = self.i
                    while s[r].isdigit():
                        r += 1
                    count = int(s[self.i:r])
                    self.i = r + 1
                    string = decode()
                    for _ in range(count):
                        ans += string
                else:
                    ans += s[self.i]
                self.i += 1
            return ans
        return decode()