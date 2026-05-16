# what if value = -1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        if matrix[0][0] > target:
            return False
        if matrix[r][0] <= target:
            l = r
        else:

            while l < r-1:
                m = (l + r) // 2
                
                


                if matrix[m][0] < target:
                    l = m
                elif matrix[m][0] > target:
                    r = m
                else:
                    return True

        # while l < r-1:
        #     m = (l + r) // 2
        #     if matrix[m][0] < target:
        #         l = m
        #     elif matrix[m][0] > target:
        #         r = m
        #     else:
        #         return True
        
        # look in matrix[l]

        searchMatrix = matrix[l]
        l = 0
        r = len(searchMatrix) - 1
        while l <= r:
            m = (l + r) // 2
            if searchMatrix[m] < target:
                l = m+1
            elif searchMatrix[m] > target:
                r = m-1
            else:
                return True
        return False
        
