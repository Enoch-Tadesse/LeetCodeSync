class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        run = [0] * (n + 1)
        output = []
        for first, last, seats in bookings:
            run[first-1] += seats
            run[last] -= seats
        # runSum = 0
        # for i in range(len(run)-1):
        #     runSum += run[i]
        #     output.append(runSum)
        # return output
        return accumulate(run[:-1])