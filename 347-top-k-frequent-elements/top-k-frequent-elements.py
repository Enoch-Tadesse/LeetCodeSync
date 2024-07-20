class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else: counter[num] += 1
        output = sorted(counter, key=lambda x: counter[x], reverse=True)
        return output[:k]