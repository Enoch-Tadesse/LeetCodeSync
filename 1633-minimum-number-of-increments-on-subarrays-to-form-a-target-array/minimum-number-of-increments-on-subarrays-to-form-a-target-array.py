class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        prev = target[0]
        updates = prev
        for num in target[1:]:
            if num > prev:
                updates += (num - prev)
            prev = num
        return updates