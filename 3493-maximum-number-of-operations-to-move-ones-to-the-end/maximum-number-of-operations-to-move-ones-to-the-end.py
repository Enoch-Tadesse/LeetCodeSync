class Solution:
    def maxOperations(self, s: str) -> int:
        counter = 0
        # when I see zero, count how many ones I have seen
        ones = 0
        last = -1
        for i, string in enumerate(s):
            if string == "1":
                if last != -1 and i - last > 1:
                    counter += ones
                ones += 1
                last = i
        if s[-1] == "0":
            counter += ones
        return counter