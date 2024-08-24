class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        # result = deque()
        result = defaultdict(int)

        # for i in range(len(nums2)-1, -1,-1):
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                result[nums2[i]] = stack[-1]
            else: result[nums2[i]] = -1
            stack.append(nums2[i])
        return [result[item] for item in nums1]
        print(result)
        # return [result[nums2.index(item)] for item in nums1]