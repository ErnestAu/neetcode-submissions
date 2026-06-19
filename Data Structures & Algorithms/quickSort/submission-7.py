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
        m = s

        for i in range(s,e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[m] = pairs[m], pairs[i]
                m += 1
            
        pairs[m], pairs[e] = pairs[e], pairs[m]

        self._quickSort(pairs, s, m-1)
        self._quickSort(pairs, m+1, e)
