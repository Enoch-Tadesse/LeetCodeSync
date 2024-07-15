class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        new_sorted = []
        new_sorted.extend(nums1[:m])
        new_sorted.extend(nums2)
        new_sorted.sort()
        for i in range(len(new_sorted)):
            nums1[i] = new_sorted[i]
        return new_sorted

                
        