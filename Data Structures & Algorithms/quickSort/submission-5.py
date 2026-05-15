# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self._quickSort(pairs, 0, len(pairs)-1)
        return pairs
    
    def _quickSort(self, pairs, s, e):
        if s >= e:
            return

        pivot = pairs[e]

        j = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                pairs[j], pairs[i] = pairs[i], pairs[j]
                j+=1
        
        pairs[j], pairs[e] = pairs[e], pairs[j]

        self._quickSort(pairs, s, j-1)
        self._quickSort(pairs, j+1, e)
