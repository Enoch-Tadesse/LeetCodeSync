class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            counts = Counter(nums[i:i + k])
            arr = [(v, k) for k , v in counts.items()]
            arr.sort(key = lambda x : (-x[0], -x[1]))
            _sum = 0
            for j in range(min(len(arr), x)):
                _sum += arr[j][0] * arr[j][1]
            ans.append(_sum)
        return ans