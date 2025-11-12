class LUPrefix:

    def __init__(self, n: int):
        self.arr = [False] * (n+1)
        self.ln = 0
        
    def upload(self, video: int) -> None:
        self.arr[video] = True
        while self.ln + 1 < len(self.arr) and self.arr[self.ln + 1]:
            self.ln += 1
        

    def longest(self) -> int:
        return self.ln