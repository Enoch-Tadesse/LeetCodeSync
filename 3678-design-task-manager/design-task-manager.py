class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.deads = defaultdict(int)
        self.relation = defaultdict(tuple)
        self.h = []
        for u, t, p in tasks:
            self.relation[t] = (u, p)
            heappush(self.h, (-p, -t, u))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.relation[taskId] = (userId, priority)
        heappush(self.h, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        u , o_p = self.relation[taskId]
        self.deads[(u,taskId, o_p)] += 1
        self.relation[taskId] = (u, newPriority)
        heappush(self.h, (-newPriority, -taskId, u))
        

    def rmv(self, taskId: int) -> None:
        u , o_p = self.relation[taskId]
        self.deads[(u,taskId, o_p)] += 1
        self.relation[taskId] = None

    def execTop(self) -> int:
        # print(self.deads)
        # print(self.h)
        while self.h:
            p, t, u = self.h[0]
            if self.deads[(u, -t, -p)] > 0:
                self.deads[(u, -t, -p)] -= 1
                heappop(self.h)
                continue
            break
        if self.h:
            ans = self.h[0][2]
            heappop(self.h)
            return ans
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()