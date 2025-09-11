class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.counter = defaultdict(int)
        self.nums = nums
        self.merge_sort(0, len(nums) - 1)
        return [self.counter[i] for i in range(len(nums))]

    def merge_sort(self, l, r):
        if l > r:
            return []
        if l == r:
            return [l]
        mid = l + (r - l) // 2
        left = self.merge_sort(l, mid)
        right = self.merge_sort(mid + 1, r)
        return self.merge(left, right)

    def merge(self, nums1: List[int], nums2: List[int]):
        i , j = 0 , 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if self.nums[nums1[i]] <= self.nums[nums2[j]]:
                self.counter[nums1[i]] += j
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        ans.extend(nums2[j:])
        while i < len(nums1):
            self.counter[nums1[i]] += j
            ans.append(nums1[i])
            i += 1
        return ans