# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


# class Solution:
#     def quickSort(self, pairs: List[Pair]) -> List[Pair]:
#         self.quickSortHelper(pairs, 0, len(pairs)-1)
#         return pairs

#     # def quickSortHelper(self,arr,s,e):
#     #     if e <= s:
#     #         return
        

#     def quickSortHelper(self, pairs, low, high):
#         if high <= low:
#             return 
        
#         pivot = pairs[high]
#         j = low
#         for i in range(low, high):
#             if pairs[i].key <= pivot.key:
#                 pairs[i], pairs[j] = pairs[j], pairs[i]
#                 j += 1
#         pairs[high], pairs[j] = pairs[j], pairs[high]
        
#         self.quickSortHelper(pairs, low, j-1)
#         self.quickSortHelper(pairs, j+1, high)


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    # Implementation of Quick Sort
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return

        pivot = arr[e] # pivot is the last element
        left = s # pointer for left side

        # Partition: elements smaller than pivot on left side
        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        # Move pivot in-between left & right sides
        arr[e] = arr[left]
        arr[left] = pivot
        
        # Quick sort left side
        self.quickSortHelper(arr, s, left - 1)

        # Quick sort right side
        self.quickSortHelper(arr, left + 1, e)
    