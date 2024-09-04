class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while stack and k > 0 and stack[-1]  > num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k-=1
        res = "".join(stack)
        res = res.lstrip("0") or "0"
        return res
        
        