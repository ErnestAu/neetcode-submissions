# 3sum

# distinct indexes
# distinct triplets

# [-1,0,1,2,-1,-4]
# sort
#     i     j k   
# [-4,-1,-1,0,1,2]



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res =set()

        for i in range(len(nums)):
            diff = 0-nums[i]
            
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j] + nums[k] < diff:
                    j+=1
                elif nums[j] + nums[k] > diff:
                    k-=1
                else:
                    res.add(tuple([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
        
        
        return [list(x) for x in list(res)]

                




            # for j in range(i+1,len(nums))
            