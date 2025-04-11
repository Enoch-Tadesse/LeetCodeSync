class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0 
        for i in range(low, high + 1):
            cand = str(i)
            if len(cand) & 1:
                continue
            cand = list(map(int, list(cand)))
            counter += int(sum(cand[:len(cand)//2]) == sum(cand[len(cand) // 2: ]))
        return counter