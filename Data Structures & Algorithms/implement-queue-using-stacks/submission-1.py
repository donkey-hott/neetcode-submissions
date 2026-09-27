class MyQueue:

    def __init__(self):
        self.in_q = []
        self.out_q = []
        
    def push(self, x: int) -> None:
        self.in_q.append(x)

    def pop(self) -> int:
        if len(self.out_q) == 0:
            for _ in range(len(self.in_q)):
                self.out_q.append(self.in_q.pop())

        return self.out_q.pop()

    def peek(self) -> int:
        if len(self.out_q) > 0:
            return self.out_q[-1]
        return self.in_q[0]

    def empty(self) -> bool:
        return len(self.in_q) + len(self.out_q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()