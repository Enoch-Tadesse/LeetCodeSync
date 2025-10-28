powers = [1 << i for i in range(0, 22)]
mod = 10 ** 9 + 7
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = 0
        nums = deliciousness
        counts = defaultdict(int)
        for num in nums:
            for p in powers:
                counter = (counter + counts[p - num]) % mod
            counts[num] += 1
        return counter % mod