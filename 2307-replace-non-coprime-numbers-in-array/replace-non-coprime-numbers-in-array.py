class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for i in range(len(nums)):
            while stack:
                cand = gcd(stack[-1], nums[i])
                if cand == 1:
                    break
                nums[i] = lcm(stack.pop(), nums[i])
            stack.append(nums[i])
        return stack