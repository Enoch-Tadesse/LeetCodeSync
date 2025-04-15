class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        self.numIdx = {num : i for i , num in enumerate(nums2)}
        self.res = [0] * n
        self.merge_sort(nums1)
        arr1 = self.res[::]
        self.res = [0] * n
        self.numIdx = {num : n - i - 1 for i , num in enumerate(nums2)}
        self.merge_sort(list(reversed(nums1)))
        arr2 = self.res[::]
        counter = 0
        for i in range(n):
            counter += arr1[i] * arr2[i]
        return counter

    def merge_sort(self, nums) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        return self.merge(self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:]))
    def merge(self, nums1, nums2):
        i , j = 0 , 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if self.numIdx[nums1[i]] < self.numIdx[nums2[j]]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                self.res[nums2[j]] += i
                j += 1
        res.extend(nums1[i:])
        while j < len(nums2):
            res.append(nums2[j])
            self.res[nums2[j]] += i
            j += 1
        return res
