class Solution:
    def check(self, nums: List[int]) -> bool:
        chances = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                chances -= 1
        if nums[len(nums)-1] > nums[0]:
            chances -=1
        return chances >= 0










        # count, N = 0, len(nums)

        # for i in range(N-1):
        #     if nums[i] > nums[(i + 1) % N]:
        #         count += 1
        #         if count > 1:
        #             return False

        # return True