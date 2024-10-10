class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res ,nums= [],[]
        def back(i,total):
            if i == len(candidates) or total > target:
                return
            if total == target:
                res.append(nums.copy())
                return
            back(i+1,total)
            
            nums.append(candidates[i])
            back(i,total+candidates[i])
            nums.pop()
            # total-=candidates[i]
        back(0,0)
        return res