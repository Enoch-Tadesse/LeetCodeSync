class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                merged_array.append(nums2[j])
                j+=1
            else:
                merged_array.append(nums1[i])
                i+=1
        while i < len(nums1):
            merged_array.append(nums1[i])
            i+=1
        while j < len(nums2):
            merged_array.append(nums2[j])
            j+=1
        n = len(merged_array)
        if n % 2 != 0:
            return merged_array[n//2]
        else:
            return float(merged_array[n/2 -1] + merged_array[n/2])/2
        