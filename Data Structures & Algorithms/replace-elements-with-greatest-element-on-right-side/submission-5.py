
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxN = -1
        for i in range(len(arr)-1,-1,-1):

            arr[i], maxN = maxN, max(maxN,arr[i])

        return arr