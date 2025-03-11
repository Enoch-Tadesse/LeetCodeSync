class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.helper(n-1)[k-1]
    def inverter(self, s):
        if s == '0':
            return '1'
        return '0'
    def helper(self, n):
        if n == 0:
            return ['0']
        curr = self.helper(n-1)
        return curr + ['1'] + list(map(self.inverter, reversed(curr)))