class TimeMap:

    def __init__(self):
        self.seen = defaultdict(lambda : list())

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.seen[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.seen[key]
        l , r = 0 , len(values) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][1] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return values[r][0] if r >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)