class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = n
        nums = flowerbed
        n = len(nums)
        counter = 0
        for i in range(n):
            if ((i-1 < 0 or nums[i-1] == 0) and (nums[i] == 0) and (i + 1 > n - 1 or nums[i+1] == 0)):
                counter += 1
                nums[i] = 1
        # print(f"{counter=} {m=}")
        return counter >= m