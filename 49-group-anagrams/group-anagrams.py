class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        the_hash = {}
        for s in strs:
            sorted_s = ("").join(sorted(s))
            if sorted_s not in the_hash:
                the_hash[sorted_s] = [s]
            else:
                the_hash[sorted_s].append(s)
        return list(the_hash.values())