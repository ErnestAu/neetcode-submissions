# what if value = -1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        e = m*n -1
        s = 0
        mid = e//2

        while s <= e:
            mid = (s+e)//2
            row = mid//n
            column = mid % n


            if matrix[row][column] > target:
                e = mid - 1
            elif matrix[row][column] < target:
                s = mid + 1
            else:
                return True
        
        return False

        # row = s//n
        # column = s % n
        # return matrix[row][column] == target
              


        
