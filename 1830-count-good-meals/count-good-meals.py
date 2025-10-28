powers = [2 ** i for i in range(0, 41)]
mod = 10 ** 9 + 7
print(powers)
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = 0
        nums = deliciousness
        nums.sort()
        counts = defaultdict(int)
        for num in nums:
            for p in powers:
                if num > p:
                    # counts[num] += 1
                    continue
                target = p - num
                # if counts[target] > 0:
                    # print(num, target, counts[target])
                counter = (counter + counts[target]) % mod
            counts[num] += 1
        return counter % mod