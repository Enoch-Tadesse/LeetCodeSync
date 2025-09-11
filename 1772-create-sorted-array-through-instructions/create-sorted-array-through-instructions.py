# keep track of the num greater than it and less than it
# during merge, if selected from the right,
# - > the index + 1 from left are the more mins
# - > the non selected from right are the more max
# consider duplicates after the count, do a linear scan and take it fro either from the mins or the maxs.
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        self.mod = 10 ** 9 + 7
        self.nums = instructions
        self._max = defaultdict(int)
        self._min = defaultdict(int)
        self.merge(0, len(self.nums) - 1)
        counter = defaultdict(int)
        ans = 0
        for i in range(len(self.nums)):
            ans = (ans + min(self._max[i], self._min[i] - counter[self.nums[i]])) % self.mod
            counter[self.nums[i]] += 1
        return ans

    def merge(self, l, r):
        if l > r:
            return []
        if l == r:
            return [l]
        mid = l + (r - l) // 2
        left = self.merge(l, mid)
        right = self.merge(mid + 1, r)
        return self.merge_sort(left, right)

    def merge_sort(self, nums1, nums2):
        i , j = 0 , 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if self.nums[nums1[i]] <= self.nums[nums2[j]]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                self._min[nums2[j]] = (self._min[nums2[j]] + i) % self.mod
                self._max[nums2[j]] = (self._max[nums2[j]] + len(nums1) - i) % self.mod
                j += 1
        ans.extend(nums1[i:])
        while j < len(nums2):
            self._min[nums2[j]] = (self._min[nums2[j]] + i) % self.mod
            ans.append(nums2[j])
            j+= 1
        return ans