class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = strs[0]
        for s in strs:
            while not s.startswith(common_prefix):
                common_prefix = common_prefix[:-1]
        return common_prefix