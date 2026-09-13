class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l, r, w = m - 1, n - 1, (m + n - 1)

        while r >= 0:
            if nums1[l] > nums2[r] and l >= 0:
                nums1[w] = nums1[l]
                l -= 1
            else:
                nums1[w] = nums2[r]
                r -= 1
            w -= 1
