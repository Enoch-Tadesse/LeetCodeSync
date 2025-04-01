class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        _maxs = [0]
        for i in range(len(questions) - 1, -1, -1):
            point , brain = questions[i][0] , questions[i][1]
            if len(_maxs) <= brain:
                _maxs.append(max(point, _maxs[-1]))
            else:
                _maxs.append(max(_maxs[-1], point + _maxs[-brain - 1]))
        return _maxs[-1]
