class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parent = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }
        stack = []
        for item in s:
            if item not in parent:
                stack.append(item)
                continue
            if len(stack) > 0 and (parent[item] == stack[-1]):
                stack.pop()
            else:
                return False
        return len(stack) == 0
