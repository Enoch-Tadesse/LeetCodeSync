class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            if char not in match:
                stack.append(char)
                continue
            if stack and match[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return False if stack else True