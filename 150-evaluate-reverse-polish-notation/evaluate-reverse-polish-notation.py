class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
                "+" : lambda x,y : x+y,
                "-" : lambda x,y : x-y,
                "*" : lambda x,y : x*y,
                "/" : lambda x,y : int(x/y)
        }
        for token in tokens:
            if token in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(operators[token](b,a))
            else: stack.append(token)
        return int(stack[0])