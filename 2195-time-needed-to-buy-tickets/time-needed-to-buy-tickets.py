class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([i for i in range(len(tickets))])

        counter = 0
        while tickets[k] > 0:
            front = q.popleft()
            tickets[front] -= 1
            if tickets[front] > 0:
                q.append(front)
            counter += 1
        return counter