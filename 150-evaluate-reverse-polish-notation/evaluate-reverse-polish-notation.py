class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"/", "+", "-", "*"}
        for token in tokens:
            if token in operators:
                mem = str(int(eval(stack[-2] + token + stack[-1])))
                stack = stack[:-2]
                stack.append(mem)
            else: stack.append(token)
        return int(stack[0])