class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, w = m - 1, n - 1, (m+n) - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1
        