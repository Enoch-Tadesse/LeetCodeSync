class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.p = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[self.p] < t - 3000:
            self.p += 1
        return len(self.q) - self.p



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)