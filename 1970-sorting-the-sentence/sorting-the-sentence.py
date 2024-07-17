class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        s_list = [(item[-1], item[0:-1]) for item in s.split(" ")]
        s_list.sort(key = lambda x : x[0])
        s_list2 = [item[1] for item in s_list]
        return (" ").join(s_list2)
        
        
        