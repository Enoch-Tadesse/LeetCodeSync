class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        def compare(n1, n2):
            if counts[n1] > counts[n2]:
                return 1
            elif counts[n1] == counts[n2] and n1 < n2:
                return 1
            return -1
        nums.sort(key=cmp_to_key(compare))
        return nums
        