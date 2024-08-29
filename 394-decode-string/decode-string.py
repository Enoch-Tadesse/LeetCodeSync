class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
                continue
            items = ""
            while stack and stack[-1] != "[":
                items = stack.pop() + items
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * items)
        return "".join(stack)