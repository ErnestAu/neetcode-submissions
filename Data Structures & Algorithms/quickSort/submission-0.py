# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# class Solution:
#     def quickSort(self, pairs: List[Pair]) -> List[Pair]:
#         self._quicksort(pairs, 0, len(pairs) - 1)
#         return pairs

#     def _quicksort(self, arr: List[Pair], lo: int, hi: int) -> None:
#         if lo >= hi:
#             return

#         pivot = arr[hi]
#         # `boundary` marks where the next "< pivot" element belongs.
#         # Everything to its left is already < pivot.
#         boundary = lo

#         for i in range(lo, hi):
#             if arr[i].key < pivot.key:
#                 arr[boundary], arr[i] = arr[i], arr[boundary]
#                 boundary += 1

#         # Drop the pivot into its final sorted slot
#         arr[boundary], arr[hi] = arr[hi], arr[boundary]

#         self._quicksort(arr, lo, boundary - 1)
#         self._quicksort(arr, boundary + 1, hi)

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs


    def quickSortHelper(self, arr: List[Pair], s:int, e:int):
        if e <= s:
            return
        
        left = s

        for i in range(s,e):
            if arr[i].key < arr[e].key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        arr[left], arr[e] = arr[e], arr[left]

        self.quickSortHelper(arr, s, left-1)
        self.quickSortHelper(arr, left+1, e)

