class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for r in range(len(s)):
            if s[r] == "]":
                temp = []
                while stack[-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                temp = "".join(reversed(temp))
                mul = []
                while stack and stack[-1].isdigit():
                    mul.append(stack.pop())
                mul = int("".join(reversed(mul)))
                if mul:
                    stack.append(mul * temp)
                else:
                    stack.append(temp)
                continue
            stack.append(s[r])
        return "".join(stack)
    