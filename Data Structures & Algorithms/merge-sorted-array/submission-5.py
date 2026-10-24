class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1, i2, w = m - 1, n - 1, m + n - 1

        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[w] = nums1[i1]
                i1 -= 1
            else:
                nums1[w] = nums2[i2]
                i2 -= 1
            w -= 1