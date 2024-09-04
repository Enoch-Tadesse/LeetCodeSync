class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # dir = []
        n = len(asteroids)
        for i in range(n):
            status = True
            # dir = Left if asteroids[i] < 0 else right
            while stack and stack[-1] > 0 and  asteroids[i] < 0:
                toright = abs(stack[-1])
                toleft = abs(asteroids[i]) 
                if toright == toleft:
                    stack.pop()
                    status = False
                    break
                if toright < toleft:
                    stack.pop()
                    continue
                if toright > toleft:
                    status = False
                    break
            if status:
                stack.append(asteroids[i])
        return stack