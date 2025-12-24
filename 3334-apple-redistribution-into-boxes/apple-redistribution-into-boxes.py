class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)

        run = 0
        i = 0
        while i < len(capacity):
            run += capacity[i]
            if run >= total:
                return i + 1
            i += 1
        return i + 1