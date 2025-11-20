class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1 # n1 comes before n2
            return 1 # n2 comes before n1
        nums.sort(key=cmp_to_key(compare))
        return str(int("".join(nums)))