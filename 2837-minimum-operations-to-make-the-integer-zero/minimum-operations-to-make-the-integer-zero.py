class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            # num1 - (sum of 2 pows) - (k * num2) = 0
            target = num1 - (k * num2)
            # can target be the sum of k 2 pow nums.
            if k > target:
                return -1
            if k >= target.bit_count():
                return k
            k += 1