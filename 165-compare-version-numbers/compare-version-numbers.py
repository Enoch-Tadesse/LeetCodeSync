class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        while v1 and v1[-1] == 0:
            v1.pop()
        while v2 and v2[-1] == 0:
            v2.pop()
        if not v1 and not v2:
            return 0
        elif not v1:
            return -1
        elif not v2:
            return 1
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        if len(v1) > len(v2):
            return 1
        elif len(v1) < len(v2):
            return -1
        return 0