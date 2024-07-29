class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        result = ""
        update = [0] * (len(s) + 1)
        for left, right, dir in shifts:
            if dir == 0:
                update[left] += -1
                update[right+1] += 1
            else:
                update[left] += 1
                update[right+1] += -1
        for k in range(1, len(update)):
            update[k] += update[k-1]
        for i in range(len(s)):
            result+= chr((ord(s[i]) - ord('a') + update[i]) % 26 + ord('a'))
        return result
            