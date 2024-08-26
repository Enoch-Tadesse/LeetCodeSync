class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sqr(num):
            return sum(int(num2)**2 for num2 in str(num))
        def helper(n, seen):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            return helper(get_sqr(n), seen)
        return helper(n, set())        
        