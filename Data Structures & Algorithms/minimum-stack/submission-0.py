class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append({ "v": val, "min_v": val if not self.st else min(val, self.getMin()) })

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]["v"]       

    def getMin(self) -> int:
        return self.st[-1]["min_v"]
        
