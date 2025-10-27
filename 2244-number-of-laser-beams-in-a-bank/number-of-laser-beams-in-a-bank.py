class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cand = []
        for b in bank:
            counts = b.count("1")
            if counts > 0:
                cand.append(counts)
        if len(cand) <= 1:
            return 0
        acc = 0
        for i in range(1, len(cand)):
            acc += cand[i] * cand[i - 1]
        return acc