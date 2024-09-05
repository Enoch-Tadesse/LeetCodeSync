class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        n = len(heights)
        for idx , height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                popped_idx = stack.pop()
                if not stack:
                    width = idx
                else:
                    width = idx - stack[-1] - 1
                largest = max(largest, heights[popped_idx] * width)
            stack.append(idx)
        print(stack)
        while stack:
            popped = stack.pop()
            if stack:
                width = (popped- stack[-1]-1) + (n-popped)
            else:
                width = n
            largest = max(largest,heights[popped]*width)
        return largest

