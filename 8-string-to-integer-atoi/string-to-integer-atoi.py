class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_dict = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9
        }
        sign = "+"
        s = s.strip()
        if s == "":
            return 0
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                s = s.replace("-", "", 1)
                sign = "-"
            else:
                s = s.replace("+", "", 1)
        if s == "":
            return 0
        if not s[0].isnumeric():
            return 0
        s_num = ""
        if not (s.isnumeric()):
            for char in s:
                if char.isnumeric():
                    s_num+=char
                else:
                    break
        else:
            s_num = s
        digit = len(s_num)-1
        final_number = 0
        for num in s_num:
            final_number = final_number + (10**digit) * num_dict[num]
            digit-=1
        if sign == "-":
            final_number = final_number * (-1)
        if final_number >= 2**31:
            return 2**31 - 1
        elif final_number < (-2)**31:
            return (-2)**31 
        else:
            return final_number

