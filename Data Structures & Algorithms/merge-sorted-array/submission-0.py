class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(len(nums1)):
            if j >= n:                    # nums2 exhausted, we're done
                return
            if nums1[i] > nums2[j] or i >= m + j:   # insert nums2[j] here
                nums1.insert(i, nums2[j])
                nums1.pop()                # remove the trailing 0 to keep length
                j += 1
