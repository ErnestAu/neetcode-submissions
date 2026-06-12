class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    result.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1

        # result = list(result)
        # for i in range(len(result)):
        #     result[i] = list(result[i])
        
        return [list(i) for i in result]
            