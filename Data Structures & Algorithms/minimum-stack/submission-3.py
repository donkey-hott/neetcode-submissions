class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_v = val if not self.st else min(val, self.st[-1][1])
        self.st.append((val, min_v))

    def pop(self) -> None:
        return self.st.pop()[0]

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
