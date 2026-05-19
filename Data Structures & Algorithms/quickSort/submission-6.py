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
        if e <= s:
            return

        pivot = pairs[e]

        j = s

        for i in range(s,e):
            if pairs[i].key < pivot.key:
                pairs[i], pairs[j] = pairs[j], pairs[i]
                j += 1
        
        pairs[e], pairs[j] = pairs[j], pairs[e]

        self._quickSort(pairs, s, j-1)
        self._quickSort(pairs, j+1, e)
