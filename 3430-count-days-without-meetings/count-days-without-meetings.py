class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # count days where emp is ava + meeting is schedules
        pre = defaultdict(int)
        pre[1] = 0
        for start, end in meetings:
            pre[start] += 1
            pre[end + 1] -= 1
        meets = [(day , weight) for day , weight in pre.items()]
        meets.sort()
        run = meets[0][1]
        counter = 0
        for i in range(1, len(meets)):
            if run == 0:
                counter += meets[i][0] - meets[i-1][0]
            run += meets[i][1]
        counter += days - meets[-1][0] + 1
        return counter