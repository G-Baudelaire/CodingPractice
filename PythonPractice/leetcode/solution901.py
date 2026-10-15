class StockSpanner:

    def __init__(self):
        self.position = -1
        self.stack = [(float("inf"), -1)]

    def next(self, price: int) -> int:
        self.position += 1
        while self.stack[-1][0] <= price:
            self.stack.pop()

        left = self.stack[-1][1]
        self.stack.append((price, self.position))
        return self.position - left
