
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        self._kClosest(points, 0, len(points)-1)
        return points[:k]
    
    def _kClosest(self, points, s, e):
        if e <= s:
            return
        
        pivotDist = math.sqrt((points[e][0])**2 + (points[e][1])**2)
        j = s
        for i in range(s,e):
            if pivotDist > math.sqrt((points[i][0])**2 + (points[i][1])**2):
                points[i], points[j] = points[j], points[i]
                j += 1
        points[e], points[j] = points[j], points[e]

        self._kClosest(points, s, j-1)
        self._kClosest(points, j+1, e)
        
        
        # minDist = math.inf
        # # return math.sqrt(0**2)
        # for i in range(len(points)):
        #     dist = math.sqrt((points[i][0])**2 + (points[i][1])**2)
        #     if dist < minDist:
        #         minDist = dist
        #         j = 0
        #         points[j] = points[i]
        #         j += 1
        #     elif dist == minDist:
        #         points[j] = points[i]
        #         j += 1
        #     else:
        #         continue


        # return points[:k]