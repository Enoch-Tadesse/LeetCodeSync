class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0:
            return False
        
        reverse = 0
        original = x

        while x > 0:
            reverse *= 10
            reverse += x % 10

            x //= 10
        return reverse == original
        