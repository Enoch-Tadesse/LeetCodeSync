class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        num_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        specials = {
            "IV" : "IIII", "CD" : "CCCC",
            "IX" : "VIIII", "CM" : "DCCCC",
            "XL" : "XXXX", "XC" : "LXXXX",
        }
        for key,value in specials.items():
            s = s.replace(key,value)
        for chars in s:
            num += num_map[chars]

        return num



