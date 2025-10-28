powers = [2 ** i for i in range(0, 22)]
mod = 10 ** 9 + 7
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = 0
        nums = deliciousness
        nums.sort()
        counts = defaultdict(int)
        for num in nums:
            for p in powers:
                if num > p:
                    continue
                target = p - num
                counter = (counter + counts[target]) % mod
            counts[num] += 1
        return counter % mod