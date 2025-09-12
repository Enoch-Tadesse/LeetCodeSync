class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e','i','o','u'}
        for w in s:
            if w in vowels:
                return True
        return False