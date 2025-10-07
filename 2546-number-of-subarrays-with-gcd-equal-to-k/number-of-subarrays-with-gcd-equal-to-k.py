class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        counter = 0
        n = len(nums)
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr = gcd(curr, nums[j])
                counter += curr == k
        return counter


            