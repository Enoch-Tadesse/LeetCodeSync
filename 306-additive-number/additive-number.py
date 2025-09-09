class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) == 2:
            return False
        for i in range(len(num)):
            first = num[:i+1]
            if first[0] == "0" and len(first) > 1:
                break
            for j in range(i + 2, len(num)):
                second = num[i+1:j]
                if second[0] == "0" and len(second) > 1:
                    break
                if self.check(num, first, second, j):
                    return True
        return False
    def check(self, num, prev, just, i):
        if i == len(num):
            return True
        next = str(int(prev) + int(just))
        starter = num[i:].find(str(next))
        if starter != 0:
            return False
        if self.check(num , just, next, starter + i + len(next)):
            return True
        return False
        
                
