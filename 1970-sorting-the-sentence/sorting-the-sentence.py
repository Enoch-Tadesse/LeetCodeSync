class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = [(item[-1], item[0:-1]) for item in s.split(" ")]
        s_list.sort()
        s_list2 = [item[1] for item in s_list]
        return (" ").join(s_list2)
        
        
        