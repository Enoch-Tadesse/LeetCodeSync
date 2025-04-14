class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.manager = defaultdict(list)
        for i , num in enumerate(manager):
            self.manager[num].append(i)
        self.res = 0
        stack = [[headID, informTime[headID]]]
        while stack:
            head, time = stack.pop()
            self.res = max(self.res, time)
            for emp in self.manager[head]:
                stack.append([emp, time + informTime[emp]])
        return self.res
