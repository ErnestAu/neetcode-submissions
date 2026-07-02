# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs)<=1:
            return pairs
        
        m = len(pairs)//2
        leftSorted = self.mergeSort(pairs[:m])
        rightSorted = self.mergeSort(pairs[m:])

        return self.merge(leftSorted,rightSorted)

    def merge(self, leftSorted, rightSorted):
        l,r = 0,0
        sortedArr = []
        while l < len(leftSorted) and r<len(rightSorted):
            if leftSorted[l].key <= rightSorted[r].key:
                sortedArr.append(leftSorted[l])
                l+=1
            else:
                sortedArr.append(rightSorted[r])
                r+=1
        
        if l < len(leftSorted):
            sortedArr.extend(leftSorted[l:])
        if r < len(rightSorted):
            sortedArr.extend(rightSorted[r:])
        
        return sortedArr