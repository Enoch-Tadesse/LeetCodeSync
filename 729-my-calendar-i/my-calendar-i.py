class MyCalendar:

    def __init__(self):
        self.nums = []    

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect_right(self.nums, (startTime, endTime))
        # if startTime == 33:
        #     print(self.nums)
        #     print(idx)
        if idx > 0:
            if self.nums[idx - 1][1] > startTime:
                return False
        if idx < len(self.nums):
            if self.nums[idx][0] < endTime:
                return False
        bisect.insort(self.nums, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)