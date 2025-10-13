class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            num = str(num)
            rev = num[::-1]
            i = 0
            while i < len(rev) and rev[i] == "0":
                i += 1
            rev = rev[i:]
            counts[num] += 1
            counts[rev] += 1
        return len(counts.keys())