class StockSpanner:

    def __init__(self):
        self.values = []
        self.st = []

    def next(self, price: int) -> int:
        self.values.append(price)
        price_idx = len(self.values) - 1
        while self.st and price >= self.values[self.st[-1]]:
            self.st.pop()
        prev_peek = -1 if not self.st else self.st[-1]
        self.st.append(price_idx)
        return price_idx - prev_peek


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)