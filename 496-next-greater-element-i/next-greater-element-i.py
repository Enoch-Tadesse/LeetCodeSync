class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        coll = defaultdict(int)
        n = len(nums2)
        for i in range(n):
            while stack and stack[-1] < nums2[i]:
                coll[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for j in range(len(nums1)):
            nums1[j] = coll.get(nums1[j], -1)
        return nums1