class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split("/")
        for p in path_list:
            if p == "..":
                if stack:
                    stack.pop()
                else : continue
            elif p == ".":
                continue
            elif p != "":
                stack.append(p)
        return ("/" + ("/").join(stack))
            