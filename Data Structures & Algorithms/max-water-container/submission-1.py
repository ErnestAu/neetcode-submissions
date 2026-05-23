
# option 1: iterate through every possible combination and find the max product 

# time complexity O(n^2)
# memory: O(1)


#  [1,7,2,5,4,7,3,6]



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        maxVolume = 0
        
        while i<j:
            maxVolume = max(
                    min(heights[i], heights[j]) * (j-i),
                    maxVolume
                ) 
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1

            

        return maxVolume