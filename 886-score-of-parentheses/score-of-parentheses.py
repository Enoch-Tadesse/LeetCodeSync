class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for string in s:
            if string == "(":
                stack.append(0)
            else:
                temp = 0
                while stack and stack[-1] != 0:
                    temp += stack.pop()
                stack.pop()
                stack.append(max(2 * temp, 1))
            # print(f"{stack=}")
        return sum(stack)
            