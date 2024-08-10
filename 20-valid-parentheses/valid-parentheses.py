class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myDic = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        for item in s:
            if item not in myDic:
                stack.append(item)
            elif len(stack) > 0 and stack[-1] == myDic[item]:
                stack.pop()
            else: return False
        if len(stack) == 0:
            return True
        return False