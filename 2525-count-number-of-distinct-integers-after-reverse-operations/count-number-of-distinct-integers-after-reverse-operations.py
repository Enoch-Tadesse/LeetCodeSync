class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        counts = set()
        for num in nums:
            counts.add(num)
            rev = 0
            first = True
            while num > 0:
                right = num % 10
                if right != 0:
                    first = False
                num //= 10
                if first and right == 0:
                    continue
                rev = rev * 10 + right
            if rev != 0:
                counts.add(rev)
        return len(counts)