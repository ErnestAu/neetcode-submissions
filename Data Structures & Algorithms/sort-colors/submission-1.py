class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt = [0] * 3
        for num in nums:
            cnt[num] += 1

        j = 0
        for i in range(3):
            for _ in range(cnt[i]):
                nums[j] = i
                j += 1
        return nums