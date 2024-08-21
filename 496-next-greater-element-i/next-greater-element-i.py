class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = deque()

        for i in range(len(nums2)-1, -1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                result.appendleft(stack[-1])
            else:
                result.appendleft(-1)
            stack.append(nums2[i])
            [7, ]
        print(result)
        return [result[nums2.index(item)] for item in nums1]