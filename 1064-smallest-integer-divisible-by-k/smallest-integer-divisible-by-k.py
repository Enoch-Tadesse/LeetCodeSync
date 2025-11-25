class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        length, number = 1, 1
        seen = set()
        while number != 0:
            if number in seen:
                return -1
            seen.add(number)
            number = (number * 10 + 1) % k
            length += 1
        return length