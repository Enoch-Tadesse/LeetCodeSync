class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = defaultdict(int)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                result[stack.pop()] = nums2[i]   
            stack.append(nums2[i])
        return [result.get(num, -1) for num in nums1]