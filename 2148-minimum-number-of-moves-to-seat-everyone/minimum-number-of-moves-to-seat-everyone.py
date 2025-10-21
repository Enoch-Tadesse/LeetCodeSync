class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        counter = 0
        for a, b in zip(seats, students):
            counter += abs(a - b)
        return counter