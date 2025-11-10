class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        ans = []
        i = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i < min(len(num1), len(num2)):
            curr = str(carry + int(num1[i]) + int(num2[i]))
            if len(curr) > 1:
                carry = int(curr[0])
            else:
                carry = 0
            ans.append(curr[-1])
            i += 1
        while i < len(num1):
            curr = str(carry + int(num1[i]))
            if len(curr) > 1:
                carry = int(curr[0])
            else:
                carry = 0
            ans.append(curr[-1])
            i += 1
        while i < len(num2):
            curr = str(carry + int(num2[i]))
            if len(curr) > 1:
                carry = int(curr[0])
            else: carry = 0
            ans.append(curr[-1])
            i += 1
        if carry != 0:
            ans.append(str(carry))
        return "".join(ans)[::-1]
            