class MyQueue:

    def __init__(self):
        self.in_st = []
        self.out_st = []

    def push(self, x: int) -> None:
        self.in_st.append(x)

    def pop(self) -> int:
        if not self.out_st:
            while self.in_st:
                self.out_st.append(self.in_st.pop())
        return self.out_st.pop()

    def peek(self) -> int:
        if not self.out_st:
            while self.in_st:
                self.out_st.append(self.in_st.pop())
        return self.out_st[-1]

    def empty(self) -> bool:
        return len(self.in_st) + len(self.out_st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()