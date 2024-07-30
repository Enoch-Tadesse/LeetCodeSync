class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        output = ""
        update = [0] *(len(s)+1)
        for left, right, dir in shifts:
            update[left] += 1 if dir == 1 else -1
            update[right + 1] +=1 if dir == 0 else -1
        for i in range(1, len(update)):
            update[i] += update[i-1]
        for i in range(len(s)):
            output+=chr(((ord(s[i])-ord('a') + update[i]) %26)+ord('a'))
        return output