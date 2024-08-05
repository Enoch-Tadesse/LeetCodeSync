class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = {}
        for index, num in enumerate(nums):
            if num in idx.keys() and (index-idx[num]) <= k:
                return True
            idx[num] = index
        return False
            