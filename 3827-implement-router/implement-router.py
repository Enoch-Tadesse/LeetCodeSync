class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.live = set()
        self.turns = deque([])
        self.by_dest = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.live:
            return False
        if len(self.live) == self.limit:
            s, d, t = self.turns.popleft()
            self.live.discard((s, d, t))
            self.by_dest[d].popleft()
        self.live.add((source, destination, timestamp))
        self.turns.append((source, destination, timestamp))
        self.by_dest[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.turns:
            return []
        s, d, t = self.turns.popleft()
        self.live.discard((s, d, t))
        self.by_dest[d].popleft()
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts = self.by_dest[destination]
        if not ts:
            return 0
        return self.bisect_right(ts, endTime) - self.bisect_left(ts, startTime)

    def bisect_right(self, arr, stamp):
        l , r = 0 , len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] <= stamp:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def bisect_left(self,arr, stamp):
        l , r = 0 , len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] >= stamp:
                r = mid - 1
            else:
                l = mid + 1
        return l


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)