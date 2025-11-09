class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        while num1 != 0 and num2 != 0:
            if (num1 >= num2):
                num1-=num2
                # x = math.ceil(num1 / num2)
                # counter += x
                # num1 -= num2 * x
            else:
                num2-=num1
                # x = math.ceil(num2 / num1)
                # print(x, math.ceil(num2 / num1))
                # counter += x
                # num2 -= num1 * x
            counter += 1
        return counter
